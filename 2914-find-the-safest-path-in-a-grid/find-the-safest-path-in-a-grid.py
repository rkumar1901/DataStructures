from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        

        n = len(grid)

        # -----------------------------------
        # 1. Multi-source BFS from all thieves
        # -----------------------------------

        dist = [[-1] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            if r > 0 and dist[r - 1][c] == -1:
                dist[r - 1][c] = dist[r][c] + 1
                queue.append((r - 1, c))

            if r + 1 < n and dist[r + 1][c] == -1:
                dist[r + 1][c] = dist[r][c] + 1
                queue.append((r + 1, c))

            if c > 0 and dist[r][c - 1] == -1:
                dist[r][c - 1] = dist[r][c] + 1
                queue.append((r, c - 1))

            if c + 1 < n and dist[r][c + 1] == -1:
                dist[r][c + 1] = dist[r][c] + 1
                queue.append((r, c + 1))

        # -----------------------------------
        # 2. Binary search for maximum safety
        # -----------------------------------

        left = 0
        right = 2 * n

        while left <= right:

            mid = (left + right) // 2

            if self.can_reach(dist, mid, n):
                left = mid + 1
            else:
                right = mid - 1

        return right

    def can_reach(self, dist, safety, n):

        if dist[0][0] < safety:
            return False

        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:

            r, c = queue.popleft()

            if r == n - 1 and c == n - 1:
                return True

            # Up
            if r > 0:
                nr, nc = r - 1, c

                if (nr, nc) not in visited and dist[nr][nc] >= safety:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            # Down
            if r + 1 < n:
                nr, nc = r + 1, c

                if (nr, nc) not in visited and dist[nr][nc] >= safety:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            # Left
            if c > 0:
                nr, nc = r, c - 1

                if (nr, nc) not in visited and dist[nr][nc] >= safety:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            # Right
            if c + 1 < n:
                nr, nc = r, c + 1

                if (nr, nc) not in visited and dist[nr][nc] >= safety:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return False
        