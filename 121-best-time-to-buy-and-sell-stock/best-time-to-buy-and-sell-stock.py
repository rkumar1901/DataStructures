class Solution(object):
    def maxProfit(self, prices):

        l = 0
        r = 0
        res = 0

        while r < len(prices):

            if prices[r] <= prices[l]:
                l = r

            else:
                res = max(res, prices[r] - prices[l])
            
            r += 1

        return res

              