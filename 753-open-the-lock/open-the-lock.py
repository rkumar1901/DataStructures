from collections import deque

class Solution(object):
    def openLock(self, deadends, target):

        dead = set(deadends)
        queue = deque([('0000', 0)])
        turns = 0
        visited = set(['0000'])

        if "0000" in dead:
            return -1

        while queue:

            curr, turns = queue.popleft()
            if curr == target:
                return turns

            for i in range(4):

                digit = int(curr[i])

                up = (digit + 1) % 10
                down = (digit - 1) % 10

                for num in [up, down]:

                    neighbor = curr[:i] + str(num) + curr[i+1:]

                    if neighbor in dead:
                        continue

                    if neighbor in visited:
                        continue

                    queue.append((neighbor, turns+1))
                    visited.add(neighbor)

        return -1





            






        