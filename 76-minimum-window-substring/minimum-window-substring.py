class Solution(object):
    def minWindow(self, s, t):

        l = 0
        countT, window = {}, {}
        reslen, res = float('inf'), [-1,-1]

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
            
        need, have = len(countT), 0
            
        for r in range(len(s)):
            
            window[s[r]] = 1 + window.get(s[r], 0)
            
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
                
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = (r - l + 1)
                    res = s[l:r + 1]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
                

        return "" if reslen == float('inf') else res


        