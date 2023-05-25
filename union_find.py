from typing import List, Dict
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self._rank = [1] * n
        self._root = [i for i in range(0, n)]
        self._count = n

    def size(self) -> int:
        return self._count

    # compress and find
    def find(self, i: int) -> int:
        if self._root[i] != i:
            self._root[i] = self.find(self._root[i])
        return self._root[i]

    # Merge by rank
    def union(self, x: int, y: int):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return

        if self._rank[xp] > self._rank[yp]:
            self._root[yp] = xp

        elif self._rank[xp] < self._rank[yp]:
            self._root[xp] = yp

        else:
            self._root[yp] = xp
            self._rank[xp] = self._rank[xp] + 1

        self._count = self._count - 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def connections(self):
        dd = {}
        for i, s in enumerate(self._root):
            if s not in dd:
                dd[s] = []
            dd[s].append(i)

        return dd


def main():
    pass


if __name__ == "__main__":
    main()
