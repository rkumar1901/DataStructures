class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        res = 0
        temp = set()

        if len(s) == 0 or len(s) == 1:
            return len(s)

        for r in range(len(s)):
            
            while s[r] in temp:
                temp.remove(s[l])
                l += 1

            temp.add(s[r])
            res = max(res, len(temp))

        return res



                    





        