class Solution:
    def jump(self, nums: list[int]) -> int:

        l = r = 0
        res = 0

        while r < len(nums) - 1:
            highest = 0

            for i in range(l, r+1):
                highest = max(highest, i + nums[i])

            l = r + 1
            r = highest
            res += 1

        return res  






        