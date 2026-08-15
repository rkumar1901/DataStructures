class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        las_pos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if (nums[i] + i) >= las_pos:
                las_pos = i

        return las_pos == 0
        