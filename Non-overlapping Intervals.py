# Problem: https://leetcode.com/problems/non-overlapping-intervals/
# Approach: Greedy - always pick the interval with the earliest end
# Time Complexity: O(n log n), Space Complexity: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # Sort by end time
        count = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                count += 1  # Overlapping, remove this

        return count
