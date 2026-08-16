from collections import deque
class Solution(object):
    def orangesRotting(self, grid):

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            
            size = len(queue)

            for _ in range(size):

                r, c = queue.popleft()

                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
            
            minutes += 1

        return -1 if fresh else minutes

            

            







        