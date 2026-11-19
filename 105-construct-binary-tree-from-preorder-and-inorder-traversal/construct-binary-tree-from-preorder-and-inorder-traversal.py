# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):

        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.pre_idx = 0

        def build(left, right):

            if left > right:
                return None

            # First element in preorder is the root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
        