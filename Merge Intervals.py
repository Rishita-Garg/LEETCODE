# Problem: https://leetcode.com/problems/merge-intervals/
# Approach: Sort intervals and merge overlapping ones
# Time Complexity: O(n log n), Space Complexity: O(n)

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])  # Merge

        return merged
