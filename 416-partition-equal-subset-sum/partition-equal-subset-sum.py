class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        # dp[s] = can we make sum s?
        dp = [False] * (target + 1)

        # Sum 0 is always possible by choosing nothing
        dp[0] = True

        for num in nums:

            for current_sum in range(target, num - 1, -1):

                previous_sum = current_sum - num

                if dp[previous_sum]:
                    dp[current_sum] = True

                    if current_sum == target:
                        return True

        return dp[target]
        