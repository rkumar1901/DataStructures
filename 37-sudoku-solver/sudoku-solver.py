class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lines = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]
        spaces = []
        # 1 find which postion we need fill(record in spaces)
        # 2 prepare lines, cols, box set array
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    spaces.append([i, j])
                else:
                    lines[i].add(x)
                    cols[j].add(x)
                    box[i//3][j//3].add(x)

        def backTrack(pos):
            if pos == len(spaces):
                return True
            # when we complete the sudoku

            i, j = spaces[pos]
            for n in ("123456789"):
                if  n not in lines[i] and n not in cols[j] and n not in box[i//3][j//3]:
                    board[i][j] = n
                    lines[i].add(n)
                    cols[j].add(n)
                    box[i//3][j//3].add(n)

                    if backTrack(pos + 1):
                        return True

                    board[i][j] = "." 
                    lines[i].remove(n)
                    cols[j].remove(n)
                    box[i//3][j//3].remove(n)
            # here we must add true, fasle return to stop the backtrack when we find one valid solution
            # this is a important difference between n queens, here only need one solution but n queens need all solution
            return False
        
        backTrack(0)    