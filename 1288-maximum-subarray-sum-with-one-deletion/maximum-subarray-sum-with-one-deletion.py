class Solution(object):
    def maximumSum(self, arr):

        n = len(arr)

        dp = [[0]*n for _ in range(2)]

        dp[0][0] = arr[0]
        dp[1][0] = float('-inf')

        result = arr[0]


        for i in range(1, n):

            dp[0][i] = max(arr[i] + dp[0][i-1], arr[i])
            
            dp[1][i] = max(dp[0][i-1], arr[i] + dp[1][i-1])

            result = max(result, dp[1][i], dp[0][i])

        return result
        