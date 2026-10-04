class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        dp = {}  # (i, buying) -> max profit

        def dfs(i, buying):

            # Base case
            if i >= len(prices):
                return 0

            # Already calculated
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Skip today
            cooldown = dfs(i + 1, buying)

            if buying:
                # Buy today
                buy = dfs(i + 1, not buying) - prices[i]

                dp[(i, buying)] = max(buy, cooldown)

            else:
                # Sell today
                sell = dfs(i + 2, not buying) + prices[i]

                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
        