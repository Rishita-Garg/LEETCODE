# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Approach: BFS using a queue
# Time Complexity: O(n), Space Complexity: O(n)

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
