"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        
        if not node:
            return None

        old_to_new = {}
        queue = deque([node])

        old_to_new[node] = Node(node.val)

        while queue:

            curr = queue.popleft()

            for neighbor in curr.neighbors:

                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                old_to_new[curr].neighbors.append(
                    old_to_new[neighbor]
                ) 

        return old_to_new[node] 
        