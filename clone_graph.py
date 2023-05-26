from typing import List, Dict
from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    graph = {}
    return dfs(node, graph)

def dfs(node: Node, graph) -> Node:
    if not node:
        return None
    if node in graph:
        return graph[node]
    copy = Node(node.val)
    graph[node] = copy
    for neighbour in node.neighbors:
        copy.neighbors.append(dfs(neighbour, graph))
    return copy


def graph_to_node(graph: List[List[int]]) -> Node:
    if len(graph) == 0:
        return None
    d = defaultdict(int)

    for val, edges in enumerate(graph):
        neighbours = []
        node = d[val + 1] if val + 1 in d else Node(val + 1)

        for edge in edges:
            neighbour = d[edge] if edge in d else Node(edge)
            neighbours.append(neighbour)
            if edge not in d:
                d[edge] = neighbour

        node.neighbors = neighbours
        d[val + 1] = node

    return d[1]


def main():
    graph1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    expected1 = graph_to_node(graph1)
    c1 = clone_graph(graph_to_node(graph1))
    print(c1)
    assert expected1 == c1

    graph2 = [[]]
    expected2 = graph_to_node(graph2)
    c2 = clone_graph(graph_to_node(graph2))
    print(c2)
    assert expected2 == c2


if __name__ == "__main__":
    main()
