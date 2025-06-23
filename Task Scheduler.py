# Problem: https://leetcode.com/problems/task-scheduler/
# Approach: Greedy with frequency count and idle slot calculation
# Time Complexity: O(n), Space Complexity: O(1)

from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_freq = max(task_counts)
        max_count = task_counts.count(max_freq)

        # Formula: (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
