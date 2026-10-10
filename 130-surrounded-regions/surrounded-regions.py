class Solution(object):
    def solve(self, board):
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"):
                return

            # Mark this O as safe
            board[r][c] = "S"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: DFS from left and right borders
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Step 2: DFS from top and bottom borders
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 3: Update the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        

        