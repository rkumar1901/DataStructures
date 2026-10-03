class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        left_to_right = 1
        right_to_left = 1
        res = 0

        for i in range(len(nums)):

            left_to_right *= nums[i]
            right_to_left *= nums[len(nums) - i - 1]

            res = max(left_to_right, right_to_left, res)

            if not left_to_right:
                left_to_right = 1
            if not right_to_left:
                right_to_left = 1

        return res



        