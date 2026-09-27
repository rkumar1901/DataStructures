class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        c = cols - 1

        while r < rows and c >= 0:

            if matrix[r][c] == target:
                return True

            elif matrix[r][c] > target:
                c = c - 1

            else:
                r = r + 1

        return False
        