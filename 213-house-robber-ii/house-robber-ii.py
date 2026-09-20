class Solution(object):
     def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Helper function: classic House Robber DP
        def rob_helper(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]

            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])

            return dp[-1]

        # Exclude last house
        loot_skipping_last = rob_helper(nums[:-1])

        # Exclude first house
        loot_skipping_first = rob_helper(nums[1:])

        return max(loot_skipping_last, loot_skipping_first)

        
        