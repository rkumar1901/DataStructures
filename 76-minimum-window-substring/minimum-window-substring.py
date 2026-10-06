class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT, window = {}, {}

        l = 0
        reslen = float('inf')
        res = ""

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        have = 0
        need = len(countT)

        for r in range(len(s)):

            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1 

            while have == need:
                if (r - l + 1) < reslen:
                    res = s[l : r + 1]
                    reslen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: 
                    have -= 1 

                l += 1

        return "" if reslen == float('inf') else res


# Time complexity: O(n)
# Space complexityL O(1) since maximum number of key can only be dictionary of 26 alphabets.








        