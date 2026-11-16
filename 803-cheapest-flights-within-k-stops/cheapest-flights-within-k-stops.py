from collections import defaultdict
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        # Step 1: Build adjacency list
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        # Step 2: Initialize distance and min heap
        distance = [[float('inf')] * (k + 2) for _ in range(n)]

        distance[src][0] = 0

        min_heap = [(0, src, 0)]

        # Step 3: Dijkstra
        while min_heap:

            cost, node, stops = heapq.heappop(min_heap)

            # Skip outdated entries
            if cost > distance[node][stops]:
                continue

            # Destination reached
            if node == dst:
                return cost

            # Maximum allowed flights = k + 1
            if stops == k + 1:
                continue

            # Explore neighbors
            for nei, price in graph[node]:

                new_cost = cost + price
                new_stops = stops + 1

                if new_cost < distance[nei][new_stops]:

                    distance[nei][new_stops] = new_cost

                    heapq.heappush(
                        min_heap,
                        (new_cost, nei, new_stops)
                    )

        return -1
        