# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def sumNumbers(self, root):

        self.queue = []
        tot = 0

        def dfs(node, temp):
            
            if not node:
                return

            temp += str(node.val)

            if not node.left and not node.right:
                self.queue.append(temp)
                return

            dfs(node.left, temp)
            dfs(node.right, temp)


        dfs(root, "")

        for i in self.queue:
            tot += int(i) 
        return tot

        
        