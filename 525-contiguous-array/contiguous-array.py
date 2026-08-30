class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_len = 0
        prefix = 0
        dic = {0 : -1}

        for r in range(len(nums)):

            if nums[r] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in dic:
                max_len = max(max_len, r - dic[prefix])

            else:
                dic[prefix] = r

        return max_len

        