class Solution:
    def uniquePathsIII(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        total = 0
        start_r = start_c = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    total += 1

                if grid[r][c] == 1:
                    start_r, start_c = r, c

        def dfs(r, c, remaining):

            # Reached end
            if grid[r][c] == 2:
                return 1 if remaining == 1 else 0

            # Mark visited
            grid[r][c] = -1

            remaining -= 1

            paths = 0

            # Down
            if r + 1 < rows and grid[r + 1][c] != -1:
                paths += dfs(r + 1, c, remaining)

            # Up
            if r - 1 >= 0 and grid[r - 1][c] != -1:
                paths += dfs(r - 1, c, remaining)

            # Right
            if c + 1 < cols and grid[r][c + 1] != -1:
                paths += dfs(r, c + 1, remaining)

            # Left
            if c - 1 >= 0 and grid[r][c - 1] != -1:
                paths += dfs(r, c - 1, remaining)

            # Backtrack
            grid[r][c] = 0

            return paths

        return dfs(start_r, start_c, total)
        