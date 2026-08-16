class Solution(object):
    def solveNQueens(self, n):

        board = [["."]*n for i in range(n)]
        diag1 = set()
        diag2 = set()
        cols = set()
        result = []

        def backtrack(r):

            if r == n:
                result.append(["".join(r) for r in board])
                return

            for c in range(n):

                if (r+c) in diag1 or (r-c) in diag2 or c in cols:
                    continue

                board[r][c] = "Q"
                diag1.add(r + c)
                diag2.add(r - c)
                cols.add(c)

                backtrack(r + 1)

                board[r][c] = "."
                diag1.remove(r + c)
                diag2.remove(r - c)
                cols.remove(c)


        backtrack(0)
        return result



        