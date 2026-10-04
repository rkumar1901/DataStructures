from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        queue = deque([0])
        visited = {0}  

        while queue:

            start = queue.popleft()

            if start == len(s):
                return True

            for end in range(start +1, len(s)+ 1):

                if end not in visited and s[start:end] in wordDict:
                    queue.append(end)
                    visited.add(end)

        return False 
        