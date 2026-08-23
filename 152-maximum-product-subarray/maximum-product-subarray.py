class Solution(object):
    def maxProduct(self, nums):
        left_right = 1
        right_left = 1
        max_p = float('-inf')
        length = len(nums)

        for i in range(length):

            left_right *= nums[i]
            right_left *= nums[length - i - 1]

            max_p = max(left_right, right_left, max_p)

            if not left_right:
                left_right = 1
            if not right_left:
                right_left = 1

        return max_p
        