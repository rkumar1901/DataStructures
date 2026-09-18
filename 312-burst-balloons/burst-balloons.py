class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length is the distance between left and right
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for k in range(left + 1, right):
                    coins = (
                        dp[left][k]
                        + nums[left] * nums[k] * nums[right]
                        + dp[k][right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        coins
                    )

        return dp[0][n - 1]
        