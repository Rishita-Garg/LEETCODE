# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Approach: DFS recursively to find max depth
# Time Complexity: O(n), Space Complexity: O(h) — h is height of tree

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
