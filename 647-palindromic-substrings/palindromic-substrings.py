class Solution:
    def countSubstrings(self, s: str) -> int:

        if len(s) == 1:
            return 1

        res = 0

        def find(l, r):

            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):

            find(i,i)
            find(i,i+1)

        return res
        