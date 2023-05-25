from typing import List
from collections import defaultdict
import heapq


def min_cost_to_supply_water(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    # bidirectional graph represented in adjacency list
    graph = defaultdict(list)

    # add a virtual vertex indexed with 0.
    #   then add an edge to each of the house weighted by the cost
    for index, cost in enumerate(wells):
        graph[0].append((cost, index + 1))

    # add the bidirectional edges to the graph
    for house_1, house_2, cost in pipes:
        graph[house_1].append((cost, house_2))
        graph[house_2].append((cost, house_1))

    # A set to maintain all the vertex that has been added to
    #   the final MST (Minimum Spanning Tree),
    #   starting from the vertex 0.
    mst_set = set([0])

    # heap to maitain the order of edges to be visited,
    #   starting from the edges originated from the vertex 0.
    # Note: we can start arbitrarily from any node.
    heapq.heapify(graph[0])
    edges_heap = graph[0]

    total_cost = 0
    while len(mst_set) < n + 1:
        cost, next_house = heapq.heappop(edges_heap)
        if next_house not in mst_set:
            # adding the new vertex into the set
            mst_set.add(next_house)
            total_cost += cost
            # expanding the candidates of edge to choose from
            #   in the next round
            for new_cost, neighbor_house in graph[next_house]:
                if neighbor_house not in mst_set:
                    heapq.heappush(edges_heap, (new_cost, neighbor_house))

    return total_cost

def main():


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
    wells3 = [5, 6, 1]
    pipes3 = [[1, 2, 2], [2, 3, 3]]
    expected3 = 6
    c3 = min_cost_to_supply_water(n3, wells3, pipes3)
    print(c3)
    assert expected3 == c3

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
    """
    """


if __name__ == "__main__":
    main()
