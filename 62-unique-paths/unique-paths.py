class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]

        return dp[n - 1]
        