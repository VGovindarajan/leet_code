from typing import List
from union_find import UnionFind


def is_valid_tree(n: int, edges: List[List[int]]) -> bool:
    uf = UnionFind(n)

    for row in edges:
        i, j = row
        # if the roots are equal we have a cycle
        if uf.find(i) == uf.find(j):
            return False
        uf.union(i, j)

    return uf.size() == 1


def main():
    tc1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    n = 5
    c1 = is_valid_tree(n, tc1)
    print(c1)

    tc2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    n = 5
    c2 = is_valid_tree(n, tc2)
    print(c2)


if __name__ == "__main__":
    main()
