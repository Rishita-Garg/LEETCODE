# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Approach: Min-heap of size k
# Time Complexity: O(n log k), Space Complexity: O(k)

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]
