class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        total_sum = sum(nums)
    
        # Validation checks
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
        
        subset_target = (target + total_sum) // 2
        
        # dp[j] stores the number of ways to form sum `j`
        dp = [0] * (subset_target + 1)
        dp[0] = 1  # Base case: 1 way to get sum 0 (empty subset)
        
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]
        