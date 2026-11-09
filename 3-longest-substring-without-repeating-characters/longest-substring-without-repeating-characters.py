class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        r = 0
        res = 0
        temp = set()

        while r < len(s):
 
            while s[r] in temp:
                temp.remove(s[l])
                l += 1 

            temp.add(s[r])
            res = max(res, len(temp))
            r += 1

        return res




                    





        