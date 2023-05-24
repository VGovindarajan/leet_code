from typing import List
from union_find import UnionFind


def earliestAcq(logs: List[List[int]], n: int) -> int:
    uf = UnionFind(n)
    logs.sort(key=lambda ll: ll[0])

    for log in logs:
        t, i, j = log
        uf.union(i, j)
        if uf.size() == 1:
            return t

    return -1


def main():
    tc1 = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
           [20190312, 1, 2], [20190322, 4, 5]]
    n = 6
    c1 = earliestAcq(tc1, n)
    print(c1)


if __name__ == "__main__":
    main()
