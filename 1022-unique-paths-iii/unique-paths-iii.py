class Solution(object):
    def uniquePathsIII(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        self.paths = 0
        total = 0
        start_r = start_c = 0

        # Count all non-obstacle cells
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] != -1:
                    total += 1

                if grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def dfs(r, c, remaining):

            # Invalid position
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == -1):
                return

            # Reached end
            if grid[r][c] == 2:
                if remaining == 1:
                    self.paths += 1
                return

            # Mark as visited
            grid[r][c] = -1
            remaining -= 1

            # Explore 4 directions
            dfs(r + 1, c, remaining)
            dfs(r - 1, c, remaining)
            dfs(r, c + 1, remaining)
            dfs(r, c - 1, remaining)

            # Backtrack
            grid[r][c] = 0

        dfs(start_r, start_c, total)

        return self.paths