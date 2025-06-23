# Problem: https://leetcode.com/problems/delete-node-in-a-bst/
# Approach: Recursively find and replace node using inorder successor
# Time Complexity: O(h), Space Complexity: O(h)

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Find inorder successor (smallest in right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root
