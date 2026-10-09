class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] 

        for r in range(len(heights)):

            while stack and heights[stack[-1]] > heights[r]:

                h = heights[stack.pop()]

                if stack:
                    width = r - stack[-1] - 1
                else:
                    width = r

                maxArea = max(maxArea, h * width)

            stack.append(r)

        # remaining stack if present will be in montonic increasing stack
        while stack:

            h = heights[stack.pop()]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            maxArea = max(maxArea, h * width)

        return maxArea

        
        