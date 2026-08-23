class Solution(object):
    def longestIncreasingPath(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r, c):

            # Outside grid
            if (r < 0 or r >= rows or
                c < 0 or c >= cols):
                return 0

            # Already calculated
            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1

            # Move down
            if r + 1 < rows and matrix[r + 1][c] > matrix[r][c]:
                longest = max(longest, 1 + dfs(r + 1, c))

            # Move up
            if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]:
                longest = max(longest, 1 + dfs(r - 1, c))

            # Move right
            if c + 1 < cols and matrix[r][c + 1] > matrix[r][c]:
                longest = max(longest, 1 + dfs(r, c + 1))

            # Move left
            if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]:
                longest = max(longest, 1 + dfs(r, c - 1))

            memo[(r, c)] = longest

            return longest

        result = 0

        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))

        return result
        