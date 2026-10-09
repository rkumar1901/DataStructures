class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        res = [0] * len(heights)
        temp = []

        for r in range(len(heights)):

            while temp and heights[temp[-1]] < heights[r]:
                j = temp.pop()
                res[j] += 1

            if temp:
                res[temp[-1]] += 1

            temp.append(r)

        return res



