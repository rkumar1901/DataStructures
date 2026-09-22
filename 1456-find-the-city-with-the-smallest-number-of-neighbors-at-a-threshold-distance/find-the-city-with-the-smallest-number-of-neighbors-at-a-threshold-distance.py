class Solution:
    def findTheCity(self, n, edges, distanceThreshold):

        INF = float("inf")

        # distance matrix
        dist = [[INF] * n for _ in range(n)]

        # Distance from a city to itself
        for i in range(n):
            dist[i][i] = 0

        # Add edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

        # Find city with minimum number of reachable cities
        result = -1
        min_count = float("inf")

        for i in range(n):

            count = 0

            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            # <= is important!
            # We want the largest city index in a tie.
            if count <= min_count:
                min_count = count
                result = i

        return result
        