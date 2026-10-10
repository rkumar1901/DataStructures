class Solution(object):
    def pacificAtlantic(self, heights):

        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):

            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
                return

            visited.add((r, c))

            if r + 1 < rows and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, visited)

            if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                dfs(r-1, c, visited)

            if c + 1 < cols and heights[r][c+1] >= heights[r][c]:
                dfs(r, c+1, visited)

            if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                dfs(r, c-1, visited)


        for r in range(rows):
            dfs(r, 0, pac)

        for r in range(rows):
            dfs(r, cols - 1, atl)
        
        for c in range(cols):
            dfs(0, c, pac)

        for c in range(cols):
            dfs(rows - 1, c, atl)


        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r,c])

        return result
            



        