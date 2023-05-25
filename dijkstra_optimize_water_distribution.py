from typing import List, Dict
from queue import PriorityQueue
from union_find import UnionFind


def get_min_pipe_cost(well_costs, home_n, adj_pipe):
    pipe_cost = well_costs.copy()
    pipe_cost_dict = {}
    if home_n not in adj_pipe:
        return pipe_cost_dict
    pipe_cost_list = adj_pipe[home_n]

    pq_pipes = PriorityQueue()
    visited = set()

    for pipe_n_fr, pipe_n_to, cost_n in pipe_cost_list:
        pq_pipes.put((cost_n, (pipe_n_fr, pipe_n_to, cost_n)))

    while not pq_pipes.empty():
        cost_p, pipe_cost_p = pq_pipes.get()
        pipe_n_fr, pipe_n_to, cost_n = pipe_cost_p
        visited.add((pipe_n_fr, pipe_n_to))

        if (pipe_n_fr, pipe_n_to) not in pipe_cost_dict:
            pipe_cost_dict[(pipe_n_fr, pipe_n_to)] = 10000000

        #print(f"current cost for home from {pipe_n_fr} to {pipe_n_to} is {pipe_cost_dict[(pipe_n_fr, pipe_n_to)]}.Incoming pipe cost is {cost_n}")
        if pipe_cost_dict[(pipe_n_fr, pipe_n_to)] > cost_p:
            pipe_cost_dict[(pipe_n_fr, pipe_n_to)] = cost_p
            print(f"set from {pipe_n_fr} to {pipe_n_to}  cost as {pipe_cost_dict[(pipe_n_fr, pipe_n_to)]}")
            for well_next_fr, well_next_to, cost_next in adj_pipe[pipe_n_to]:
                pq_pipes.put((cost_next, (well_next_fr, well_next_to, cost_next)))

    print("pipe_cost_dict", pipe_cost_dict)
    return pipe_cost_dict

def get_piping_cost(wells, piping_cost, homes_to_connect):
    visited = set()
    connected = set()
    required = set(homes_to_connect)
    calc_cost = 0
    pq = PriorityQueue()
    if len(piping_cost) == 0:
        return calc_cost
    for k, v in piping_cost.items():
        pq.put((v, k))

    stop = False
    uf = UnionFind(len(homes_to_connect))
    while not pq.empty() and not stop:
        cost, fr_to = pq.get()
        fr, to = fr_to
        to_fr = (to, fr)
        if fr_to not in visited or to_fr not in visited:
            visited.add(fr_to)
            visited.add(to_fr)
            from_well_cost = wells[fr-1]
            to_well_cost = wells[to-1]
            max_well_cost = max(from_well_cost, to_well_cost)
            curr_cost = min(cost, max_well_cost)
            calc_cost += curr_cost
            connected.add(fr)
            connected.add(to)
            uf.union(homes_to_connect.index(fr),homes_to_connect.index(to))
            print(f"Connected {fr} to {to} with pipe cost {curr_cost}")
            if uf.size() == 1:
                stop = True

    return calc_cost


def min_cost_to_supply_water(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    print('Starting .....')
    uf = UnionFind(n + 1)

    for pipe in pipes:
        uf.union(pipe[0], pipe[1])
    conn = uf.connections()

    # Set up the adjacency matrix
    adj_pipe = {}
    for pipe in pipes:
        fr, to, co = pipe
        if fr not in adj_pipe:
            adj_pipe[fr] = []
        if to not in adj_pipe:
            adj_pipe[to] = []
        adj_pipe[fr].append((fr, to, co ))
        adj_pipe[to].append((to, fr, co ))

    # Set up the PQ with well costs
    pq = PriorityQueue()
    well_cost = [0] * (n + 1)
    default_pipe_cost = [0] * (n + 1)
    home_cost = [0] * (n + 1)
    final_cost = 0

    for well_i, cost_i in enumerate(wells):
        pq.put((cost_i, (well_i + 1)))
        well_cost[well_i + 1] = cost_i
        default_pipe_cost[well_i + 1] = cost_i
        home_cost[well_i + 1] = cost_i

    visited_well = set()
    while not pq.empty():
        cost_i, well_i = pq.get()
        print(f"starting well {well_i}")
        if well_i in visited_well:
            print(f" well {well_i} already visited")
            continue
        visited_well.add(well_i)
        well_root = uf.find(well_i)
        connected_homes = conn[well_root]

        pipe_costs = get_min_pipe_cost(default_pipe_cost, well_root, adj_pipe)
        print("before pipe_costs", pipe_costs)
        piping_cost = get_piping_cost(wells, pipe_costs, connected_homes)
        final_cost += cost_i + piping_cost
        print(f'Connected {connected_homes} with pipes costing {piping_cost}. Well cost : {cost_i}. Final Cost : {final_cost}')
        for c in connected_homes:
            if c == well_i:
                continue
            visited_well.add(c)

    print(final_cost)
    return final_cost


def main():
    """
    n1 = 3
    wells1 = [1, 2, 2]
    pipes1 = [[1, 2, 1], [2, 3, 1]]
    expected1 = 3
    c1 = min_cost_to_supply_water(n1, wells1, pipes1)
    print(c1)
    assert expected1 == c1

    n2 = 2
    wells2 = [1, 1]
    pipes2 = [[1, 2, 1], [1, 2, 2]]
    expected2 = 2
    c2 = min_cost_to_supply_water(n2, wells2, pipes2)
    print(c2)
    assert expected2 == c2

    n3 = 3
    wells3 = [5, 5, 1]
    pipes3 = [[1, 2, 2], [2, 3, 3]]
    expected3 = 6
    c3 = min_cost_to_supply_water(n3, wells3, pipes3)
    print(c3)
    assert expected3 == c3

    """
    n4 = 5
    wells4 = [46012, 72474, 64965, 751, 33304]
    pipes4 = [[2, 1, 6719], [3, 2, 75312], [5, 3, 44918]]
    expected4 = 131704
    c4 = min_cost_to_supply_water(n4, wells4, pipes4)
    print(c4)
    assert expected4 == c4

    n5 = 6
    wells5 = [4625, 65696, 86292, 68291, 37147, 7880]
    pipes5 = [[2, 1, 79394], [3, 1, 45649], [4, 1, 75810], [5, 3, 22340], [6, 1, 6222]]
    expected5 = 204321
    c5 = min_cost_to_supply_water(n5, wells5, pipes5)
    print(c5)
    assert expected5 == c5


if __name__ == "__main__":
    main()
