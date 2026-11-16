import heapq

class Solution(object):
    def swimInWater(self, grid):

        n = len(grid)

        visited = set()
        min_heap = [(grid[0][0], 0, 0)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:

            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Destination reached
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and
                    0 <= nc < n and
                    (nr, nc) not in visited):

                    new_time = max(time, grid[nr][nc])

                    heapq.heappush(
                        min_heap,
                        (new_time, nr, nc)
                    )

        return -1
        