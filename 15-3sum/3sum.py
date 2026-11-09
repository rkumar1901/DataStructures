class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        res = set()

        for idx, num in enumerate(nums):

            if idx > 0 and num == nums[idx-1]:
                continue

            l = idx+1
            r = len(nums) - 1

            while l < r:
                
                sum = nums[l] + num + nums[r]
                
                if sum > 0:
                    r -= 1
                
                elif sum < 0:
                    l += 1

                else:
                    res.add((nums[l], num, nums[r]))
                    l += 1
                    r -= 1

        return list(res)







        