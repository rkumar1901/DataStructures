class Solution(object):
    def getMaximumGold(self, grid):

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        self.max_gold = 0

        def dfs(r, c, gold):
            # Out of bounds, no gold, or already visited
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited):
                return

            visited.add((r, c))
            gold += grid[r][c]

            self.max_gold = max(self.max_gold, gold)

            # Explore
            dfs(r + 1, c, gold)
            dfs(r - 1, c, gold)
            dfs(r, c + 1, gold)
            dfs(r, c - 1, gold)

            # Backtrack
            visited.remove((r, c))

        # Try every gold cell as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    dfs(r, c, 0)

        return self.max_gold
        