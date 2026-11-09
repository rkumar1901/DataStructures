class Solution(object):
    def trap(self, height):

        l = 0
        r = len(height) - 1
        res = 0
        leftmax = 0
        rightmax = 0

        while l < r:

            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])

            if leftmax > rightmax:
                res += rightmax - height[r]
                r -= 1

            else:
                res += leftmax - height[l]
                l += 1

        return res


        