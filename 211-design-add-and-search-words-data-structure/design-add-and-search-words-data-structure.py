class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word):
        
        def dfs(index, node):

            if index == len(word):
                return node.isWord

            ch = word[index]

            if ch != ".":
                if ch not in node.children:
                    return False

                return dfs(index+1, node.children[ch])

            for child in node.children.values():
                if dfs(index+1, child):
                    return True

            return False

        dfs(0, self.root)

        return dfs(0, self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)