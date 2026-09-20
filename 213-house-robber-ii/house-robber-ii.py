class Solution(object):
     def rob(self, nums):
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]

        # # Helper function: classic House Robber DP
        # def rob_helper(houses):
        #     n = len(houses)
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return houses[0]

        #     dp = [0] * n
        #     dp[0] = houses[0]
        #     dp[1] = max(houses[0], houses[1])

        #     for i in range(2, n):
        #         dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])

        #     return dp[-1]

        # # Exclude last house
        # loot_skipping_last = rob_helper(nums[:-1])

        # # Exclude first house
        # loot_skipping_first = rob_helper(nums[1:])

        # return max(loot_skipping_last, loot_skipping_first)


        if len(nums) == 1:
            return nums[0]

        def rob_linear(start, end):
            prev2 = 0
            prev1 = 0

            for i in range(start, end):
                current = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            rob_linear(0, len(nums) - 1),  # exclude last
            rob_linear(1, len(nums))       # exclude first
        )

        
        