# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Approach: Recursive inorder (Left ➝ Root ➝ Right)
# Time Complexity: O(n), Space Complexity: O(n) for recursion stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result
