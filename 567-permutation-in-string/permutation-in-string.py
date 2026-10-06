class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):

            count2[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) > len(s1):
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if count1 == count2:
                return True

        return False

