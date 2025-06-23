# Problem: https://leetcode.com/problems/linked-list-cycle/
# Approach: Floyd’s Cycle Detection Algorithm (Tortoise and Hare)
# Time Complexity: O(n), Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
