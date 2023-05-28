from typing import List
from collections import defaultdict, deque


def find_itinerary1(tickets: List[List[str]]) -> List[str]:
    visited = []
    itinerary = []
    adj = defaultdict(list)
    start = "JFK"
    itinerary.append(start)

    for ticket in tickets:
        dep, arr = ticket
        adj[dep].append(arr)

    stack = deque()
    stack.append(start)

    while stack:
        dep = stack.pop()
        dep_list = adj[dep]
        dep_list.sort(key=lambda x: x.lower())
        for arr_to in dep_list:
            route = [dep, arr_to]
            if arr_to not in adj and len(visited) != len(tickets)-1:
                continue
            visited.append(route)
            itinerary.append(arr_to)
            stack.append(arr_to)
            dep_list.remove(arr_to)
            break

    return itinerary


# https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3901/discuss/78768/Short-Ruby-Python-Java-C++
def find_itinerary(tickets: List[List[str]]) -> List[str]:
    targets = defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a].append(b)
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack.append(targets[stack[-1]].pop())
        route.append(stack.pop())
    return route[::-1]


def main():
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    expected1 = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    c1 = find_itinerary(tickets1)
    print(c1)
    assert expected1 == c1

    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    expected2 = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    c2 = find_itinerary(tickets2)
    print(c2)
    assert expected2 == c2

    tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    expected3 = ["JFK", "NRT", "JFK", "KUL"]
    c3 = find_itinerary(tickets3)
    print(c3)
    assert expected3 == c3


if __name__ == "__main__":
    main()
