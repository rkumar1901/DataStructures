class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        cols = len(matrix[0])
        rows = len(matrix)
        
        l = 0
        r = (rows * cols) - 1

        while l <= r:

            mid = (l + r) // 2

            temp_r = mid // cols
            temp_c = mid % cols

            if target == matrix[temp_r][temp_c]:
                return True

            elif target > matrix[temp_r][temp_c]:
                l = mid + 1
            
            else:
                r = mid - 1

        return False
        