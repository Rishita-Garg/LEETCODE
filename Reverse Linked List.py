# Problem: https://leetcode.com/problems/reverse-linked-list/
# Approach: Iterative using 3 pointers (prev, curr, next)
# Time Complexity: O(n), Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev       # Reverse current node's pointer
            prev = curr            # Move prev and curr one step forward
            curr = next_node
            
        return prev
