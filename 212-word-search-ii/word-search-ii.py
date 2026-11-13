class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWords(self, word):
        curr = self

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]
        
        curr.isWord = True
        

class Solution(object):
    def findWords(self, board, words):

        root = TrieNode()
        for word in words:
            root.addWords(word)

        rows = len(board)
        cols = len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node, word):

            if (r < 0 or r >=rows or c >= cols or c < 0 or (r,c) in visited or board[r][c] not in node.children):
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord = False

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(res)



        
        