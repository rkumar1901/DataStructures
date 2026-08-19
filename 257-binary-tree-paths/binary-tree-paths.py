# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        self.res = []

        def dfs(node, temp):

            if not node:
                return

            temp += str(node.val)

            if not node.left and not node.right:
                self.res.append(temp)
                return

            temp += "->"

            dfs(node.left, temp)
            dfs(node.right, temp)

        dfs(root, "")
        return self.res
        