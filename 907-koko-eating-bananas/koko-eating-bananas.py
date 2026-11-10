class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        

        while l < r:

            mid = (l + r) // 2
            hour = 0

            for p in piles:
                hour += math.ceil(p / mid)

            if hour > h:
                l = mid + 1

            else:
                r = mid

        return l  
