class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        n = len(heights)
        res = [0] * n
        stack = []

        for i in range(n):

            while stack and heights[stack[-1]] < heights[i]:
                j = stack.pop()
                res[j] += 1

            if stack:
                res[stack[-1]] += 1

            stack.append(i) 

        return res
        