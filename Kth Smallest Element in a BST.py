# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Approach: Inorder traversal (gives sorted order)
# Time Complexity: O(k), Space Complexity: O(h)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None

        def inorder(node):
            if not node or self.res is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res
