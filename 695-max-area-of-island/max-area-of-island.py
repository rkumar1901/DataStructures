class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        self.max_area = 0
        self.area = 0
        rows = len(grid)
        cols = len(grid[0])
        fin_area = 0

        def dfs(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 

            self.area += 1
            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            return self.area
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.area = 0
                    dfs(r,c)
                    self.max_area = max(self.area, self.max_area)
                    

        return self.max_area