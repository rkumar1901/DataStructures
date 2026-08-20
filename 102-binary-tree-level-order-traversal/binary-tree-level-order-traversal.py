# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def levelOrder(self, root):

        res = [[]]
        if not root:
            return []

        def dfs(root, level):

            if not root:
                return

            if len(res) == level:
                res.append([])

            res[level].append(root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        

        dfs(root, 0)
        return res



