class Solution(object):
    def maxArea(self, height):

        max_vol = 0
        l = 0
        r = len(height) - 1
        nums = height

        while l < r:

            vol = min(nums[r], nums[l]) * (r - l)
            max_vol = max(vol, max_vol)

            if nums[r] > nums[l]:
                l += 1
            else:
                r -= 1

        return max_vol


        