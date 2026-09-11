class Solution(object):
    def twoSum(self, numbers, target):
        
        n = numbers
        l = 0
        r = len(n) - 1

        while l < r:

            if n[r] + n[l] > target:
                r -= 1
            elif n[r] + n[l] < target:
                l += 1
            else:
                return [l+1,r+1]
        