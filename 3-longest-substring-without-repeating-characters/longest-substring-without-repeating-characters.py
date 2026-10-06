class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        r = 0
        temp = set()
        res = 0

        if len(s) == 0 or len(s) == 1:
            return len(s)

        while r < len(s):

            while s[r] in temp:
                temp.remove(s[l])
                l += 1

            temp.add(s[r])
            res = max(len(temp), res)
            r += 1

        return res




                    





        