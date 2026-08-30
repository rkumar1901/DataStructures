class Solution(object):
    def checkSubarraySum(self, nums, k):
        hashmap = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in hashmap:
                if i - hashmap[remainder] >= 2:
                    return True
            else:
                hashmap[remainder] = i

        return False
        