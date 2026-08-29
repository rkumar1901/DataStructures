# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):

        stack = []

        for num in nums:

            node = TreeNode(num)

            while stack and stack[-1].val < num:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]


        