class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for r in range(9)]
        cols = [set() for c in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        spaces = []

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    spaces.append((r, c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[r//3][c//3].add(board[r][c])


        def backtrack(pos):
            if pos == len(spaces):
                return True

            i, j = spaces[pos]
            
            for num in "123456789":

                if num not in rows[i] and num not in cols[j] and num not in boxes[i//3][j//3]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[i//3][j//3].add(num)

                    if backtrack(pos + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[i//3][j//3].remove(num)

            return False

        backtrack(0)

                    




