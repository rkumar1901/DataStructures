from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:

            curr, length = queue.popleft()

            if curr == endWord:
                return length

            for i in range(len(curr)):
                for j in "abcdefghijklmnopqrstuvwxyz":

                    newWord = curr[:i] + j + curr[i+1:]
                    
                    if newWord not in wordList:
                        continue
                    
                    queue.append([newWord, length + 1])
                    wordList.remove(newWord)

        return 0



        