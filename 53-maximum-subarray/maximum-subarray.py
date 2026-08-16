class Solution(object):
    def maxSubArray(self, nums):

        if len(nums) == 1:
            return nums[0]

        max_val = float('-inf')
        sub = 0

        for i in nums:

            if sub < 0:
                sub = 0

            sub += i
            max_val = max(max_val, sub)

        return max_val



        