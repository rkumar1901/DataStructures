class Solution(object):
    def twoSum(self, nums, target):

        dic = {}

        for idx,num in enumerate(nums):

            if target - num in dic:
                return [idx, dic[target-num]]

            dic[num] = idx

        