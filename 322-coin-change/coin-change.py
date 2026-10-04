class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0 # since we can make 0 amount with 0 coins

        for i in range(amount + 1):
            for c in coins:

                if i - c >= 0:
                    dp[i] = min(1 + dp[i-c], dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1
         