class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dic1, dic2 = {},{}
        
        for i in s:
            dic1[i] = 1 + dic1.get(i, 0)

        for j in t:
            dic2[j] = 1 + dic2.get(j, 0)

        return dic1 == dic2
        