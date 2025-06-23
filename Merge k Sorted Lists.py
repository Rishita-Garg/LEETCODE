# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Approach: Min-heap to merge k sorted linked lists
# Time Complexity: O(N log k), Space Complexity: O(k)

from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Define comparator for heap
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        heap = []
        for l in lists:
            if l:
                heappush(heap, l)

        dummy = ListNode()
        curr = dummy

        while heap:
            node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, node.next)

        return dummy.next
