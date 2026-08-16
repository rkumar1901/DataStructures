class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        res = set()

        for i,num in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                tot = nums[l] + nums[i] + nums[r]

                if tot == 0:
                    res.add((nums[l],nums[i],nums[r]))
                    l += 1
                    r -= 1

                elif tot > 0:
                    r -= 1

                else:
                    l += 1

        return list(res)



        