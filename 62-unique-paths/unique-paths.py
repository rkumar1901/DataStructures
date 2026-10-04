class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # board = [[1]*n for i in range(m)]

        # for r in range(1, m):
        #     for c in range(1, n):
                
        #         board[r][c] = board[r-1][c] + board[r][c-1]

        # return board[m-1][n-1]
        
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]

        return dp[-1] 

        