class Solution(object):
    def maxProfit(self, prices):
        
        if len(prices) == 1:
            return 0

        l = 0
        r = 1
        res = 0

        while r < len(prices):

            res = max(res, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r

            r += 1

        return res
        