class Solution(object):
    def rob(self, nums):

        # if len(nums) == 1:
        #     return nums[0] 

        # def find(nums):

        #     n = len(nums)

        #     if n == 1:
        #         return nums[0]

        #     dp = [0] * len(nums)

        #     dp[0] = nums[0]
        #     dp[1] = max(nums[0], nums[1])

        #     for i in range(2, len(nums)):
        #         dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
        #     return dp[-1]

        # ans1 = find(nums[1:])
        # ans2 = find(nums[:-1])

        # return max(ans1, ans2)


        if len(nums) == 1:
            return nums[0]

        def find(nums):

            prev1 = 0
            prev2 = 0

            for i in range(len(nums)):

                current = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = current

            return prev1

        return max(find(nums[1:]), find(nums[:-1]))