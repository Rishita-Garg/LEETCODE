# Problem: https://leetcode.com/problems/validate-binary-search-tree/
# Approach: Recursively ensure node values are in valid range (min < node < max)
# Time Complexity: O(n), Space Complexity: O(h) — h = height of tree

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, float('-inf'), float('inf'))
