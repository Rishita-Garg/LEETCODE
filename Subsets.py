# Problem: https://leetcode.com/problems/subsets/
# Approach: Backtracking - include/exclude each element
# Time Complexity: O(2^n), Space Complexity: O(n)

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])  # Copy the current subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
