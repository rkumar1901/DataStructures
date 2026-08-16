# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):

        tot = 0
        temp = ""
        queue = []

        def add(node, temp, queue):

            if not node:
                return

            temp += str(node.val)

            # If this is a leaf, save the number
            if not node.left and not node.right:
                queue.append(temp)
                return

            add(node.left, temp, queue)
            add(node.right, temp, queue)

        add(root, temp, queue)

        for i in queue:
            tot += int(i)

        return tot

        
        