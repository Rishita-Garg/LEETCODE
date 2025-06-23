# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Approach: BST property — move left or right based on values
# Time Complexity: O(h), Space Complexity: O(1)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
