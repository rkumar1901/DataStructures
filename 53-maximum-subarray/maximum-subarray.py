class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        res = float('-inf')
        temp = 0

        for num in nums:

            if temp < 0:
                temp = 0

            temp += num

            res = max(temp, res)

        return res

        