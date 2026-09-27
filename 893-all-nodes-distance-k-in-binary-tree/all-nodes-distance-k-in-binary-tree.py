# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        parent = {}

        def dfs(node, par):

            if not node:
                return

            parent[node] = par

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        queue = deque([(target, 0)])
        visited = {target}


        while queue:
            
            node, distance = queue.popleft()

            if distance == k:
                return [node.val for node, _ in queue] + [node.val]

            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append([node.left, distance+1])

            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append([node.right, distance+1])

            if parent[node] and parent[node] not in visited:
                visited.add(parent[node])
                queue.append([parent[node], distance+1])

        return []
        