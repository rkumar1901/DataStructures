class Solution(object):
    def minSubArrayLen(self, target, nums):

        l = 0
        prefix = 0
        res = float('inf')

        for r in range(len(nums)):
            prefix += nums[r]

            while prefix >= target:
                res = min(res, r - l + 1)
                prefix -= nums[l]
                l += 1

            

        if res == float('inf'):
            return 0
        else:
            return res    
