import heapq
class Solution:
    def minCostConnectPoints(self, points):

        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point)
        total_cost = 0

        while min_heap:

            cost, point = heapq.heappop(min_heap)

            if point in visited:
                continue

            visited.add(point)
            total_cost += cost

            if len(visited) == n:
                return total_cost

            x1, y1 = points[point]

            for nei in range(n):
                if nei not in visited:

                    x2, y2 = points[nei]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (distance, nei))

        return total_cost
        