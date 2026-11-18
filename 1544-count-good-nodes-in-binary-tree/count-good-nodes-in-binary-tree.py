# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):

        self.good = 0

        def find(node, max_so_far):
            
            if not node:
                return 0

            if node.val >= max_so_far:
                self.good += 1

            max_so_far = max(node.val, max_so_far)

            l = find(node.left, max_so_far)
            r = find(node.right, max_so_far)
    
        find(root, float('-inf'))
        return self.good
        