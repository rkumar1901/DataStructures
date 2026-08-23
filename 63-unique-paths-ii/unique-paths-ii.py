class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0]*cols for _ in range(rows)]

        if grid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for c in range(1, cols):
            if grid[0][c] == 0:
                dp[0][c] = dp[0][c-1]

        for r in range(1, rows):
            if grid[r][0] == 0:
                dp[r][0] = dp[r-1][0]

        for r in range(1, rows):
            for c in range(1, cols):

                if grid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[rows-1][cols-1]


        

            
        