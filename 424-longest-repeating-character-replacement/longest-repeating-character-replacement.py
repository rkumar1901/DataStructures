class Solution(object):
    def characterReplacement(self, s, k):

        l = 0
        dic = {}
        res = 0

        for r in range(len(s)):

            dic[s[r]] = 1 + dic.get(s[r], 0)

            if (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res










