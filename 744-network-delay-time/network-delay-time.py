from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)

        for u,v,weight in times:
            graph[u].append((v, weight))

        visited = set()
        min_heap = [(0, k)]
        max_dist = 0

        while min_heap:

            dist, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            else:
                visited.add(node)

            max_dist = max(max_dist, dist)

            for nei,weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (weight+dist, nei))

        if len(visited) != n:
            return -1

        return max_dist





        