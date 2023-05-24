from typing import List
from collections import defaultdict, deque


def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj = {}
    n, m, qn = len(equations), len(values), len(queries)
    if n != m:
        return [-1] * n

    for i in range(0, n):
        a, b = equations[i]
        val = values[i]
        if a not in adj:
            adj[a] = []
        if b not in adj:
            adj[b] = []
        adj[a].append((b, val))
        adj[b].append((a, 1 / val))

    ans = [-1] * qn
    to_eval = []
    for i in range(0, qn):
        a, b = queries[i]
        if a not in adj or b not in adj:
            continue
        if a == b:
            ans[i] = 1
            continue
        to_eval.append(i)

    for i in to_eval:
        query = queries[i]
        nr = query[0]
        dr = query[1]
        visited = set()
        visited.add(nr)
        q = deque()
        q.append((nr, 1))
        found = False
        while q and not found:
            drc, val = q.pop()
            visited.add(drc)

            if drc == dr:
                ans[i] = val
                found = True
            else:
                for bv in adj[drc]:
                    if bv[0] not in visited:
                        calc_val = val * bv[1]
                        q.append((bv[0], calc_val))

    return ans


def main():
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected1 = [6.0, 0.5, -1.0, 1.0, -1.0]
    c1 = calc_equation(equations1, values1, queries1)
    print(c1)
    assert expected1 == c1

    equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values2 = [1.5, 2.5, 5.0]
    queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected2 = [3.75000, 0.40000, 5.00000, 0.20000]
    c2 = calc_equation(equations2, values2, queries2)
    print(c2)
    assert expected2 == c2

    equations3 = [["a", "b"]]
    values3 = [0.5]
    queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected3 = [0.50000, 2.00000, -1.00000, -1.00000]
    c3 = calc_equation(equations3, values3, queries3)
    print(c3)
    assert expected3 == c3


if __name__ == "__main__":
    main()
