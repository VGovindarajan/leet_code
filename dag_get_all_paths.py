from typing import List
from collections import defaultdict, deque


def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    visited = []
    paths = []
    adj = defaultdict(list)
    last_node = 0
    for index, edges in enumerate(graph):
        last_node = index
        for edge in edges:
            adj[index].append(edge)

    stack = deque()
    start = [0]
    stack.append(start)

    while stack:
        last_route = stack.popleft()
        last_vertex = last_route[-1]
        visited.append(last_route)
        if last_vertex == last_node:
            paths.append(last_route)
            continue
        if last_vertex not in adj:
            continue
        for new_vertex in adj[last_vertex]:
            if new_vertex in last_route:
                continue
            new_route = last_route.copy()
            new_route.append(new_vertex)
            if new_route not in visited:
                stack.append(new_route)
    return paths


def main():
    """
    graph1 = [[1, 2], [3], [3], []]
    expected1 = [[0, 1, 3], [0, 2, 3]]
    c1 = all_paths_source_target(graph1)
    print(c1)
    assert expected1 == c1
    """
    graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected2 = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    #           [[0, 4], [0, 3, 4], [0, 1, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
    c2 = all_paths_source_target(graph2)
    print(c2)
    assert expected2 == c2


if __name__ == "__main__":
    main()
