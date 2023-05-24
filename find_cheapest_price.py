from typing import List
import queue


def find_cheapest_price_bellman_ford(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(0, k + 1):
        temp_prices = prices.copy()

        for j in flights:
            s, d, p = j
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < temp_prices[d]:
                temp_prices[d] = prices[s] + p
        prices = temp_prices

    return -1 if prices[dst] == float("inf") else prices[dst]


def find_cheapest_priced_dfs(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = {}
    for i in flights:
        fr, to, di = i
        if fr not in adj:
            adj[fr] = []
        adj[fr].append([to, di])

    prices = [float("inf")] * n
    prices[src] = 0
    stops = 0
    q = queue.Queue()
    q.put([src, 0])

    while stops <= k and q:
        dest_t, dist_t = q.get()
        if dest_t not in adj:
            continue
        for m in adj[dest_t]:
            dest_m, dist_m = m

            if dist_t + dist_m < prices[dest_m]:
                prices[dest_m] = dist_t + dist_m
                q.put([dest_m, prices[dest_m]])

        stops += 1
    return -1 if prices[dst] is float("inf") else prices[dst]


def find_cheapest_priced_dijkstra(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = {}
    for i in flights:
        fr, to, di = i
        if fr not in adj:
            adj[fr] = []
        adj[fr].append([to, di])

    prices = [float("inf")] * n
    prices[src] = 0
    stops = 0
    q = queue.PriorityQueue()
    q.put((0, [0, src, 0]))

    while stops <= k and q:
        ll = q.get()
        dist_t, dest_t, dist_stops = ll[1]

        # missing in adj list
        if dest_t not in adj:
            continue
        # We have seen this earlier
        if dist_stops < stops:
            continue
        # we have exceeded the number of stops
        if dist_stops > k:
            continue

        for m in adj[dest_t]:
            dest_m, dist_m = m
            if dist_t + dist_m < prices[dest_m]:
                prices[dest_m] = dist_t + dist_m
                q.put((prices[dest_m], [prices[dest_m], dest_m, dist_stops + 1]))

        stops += 1
    return -1 if prices[dst] is float("inf") else prices[dst]


def main():
    cities = 5
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200], [2, 4, 200], [3, 4, 200]]
    start = 0
    destination = 4
    max_stops = 3

    cheapest_price = find_cheapest_price_bellman_ford(cities, flights, start, destination, max_stops)
    print(cheapest_price)
    cheapest_price = find_cheapest_priced_dfs(cities, flights, start, destination, max_stops)
    print(cheapest_price)

    cheapest_price = find_cheapest_priced_dijkstra(cities, flights, start, destination, max_stops)
    print(cheapest_price)


if __name__ == "__main__":
    main()
