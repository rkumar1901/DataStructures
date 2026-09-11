class Solution(object):
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r:
            
            mid = (l + r) // 2

            temp_r = mid // cols
            temp_c = mid % cols

            if matrix[temp_r][temp_c] > target:
                r = mid - 1

            elif matrix[temp_r][temp_c] < target:
                l = mid + 1

            else:
                return True

        return False



        