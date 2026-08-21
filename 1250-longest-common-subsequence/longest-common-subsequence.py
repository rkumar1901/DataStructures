class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        m, n = len(text1), len(text2)
        
        # Ensure text2 is the shorter string to minimize space complexity to O(min(M, N))
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
            
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):
            prev = 0  # Represents dp[i-1][j-1]
            
            for j in range(1, n + 1):
                temp = dp[j]  # Save old dp[i-1][j] before overwriting
                
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                    
                prev = temp  # Update prev for the next column calculation
                
        return dp[n]

        