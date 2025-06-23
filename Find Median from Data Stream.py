# Problem: https://leetcode.com/problems/find-median-from-data-stream/
# Approach: Two Heaps — Max-heap (low) and Min-heap (high)
# Time Complexity: O(log n) per insert, O(1) median, Space: O(n)

import heapq

class MedianFinder:

    def __init__(self):
        self.low = []  # Max heap (invert values)
        self.high = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
