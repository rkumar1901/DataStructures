class Solution(object):
    def longestPalindrome(self, s):

        if len(s) == 1:
            return s
        
        res = ""

        def expand(l, r, temp):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]

        for i in range(len(s)):

            ans1 = expand(i, i, "")
            ans2 = expand(i, i+1, "")

            res = max(ans1, ans2, res, key=len)

        return res
         
        