# Problem: https://leetcode.com/problems/combination-sum/
# Approach: Backtracking with choice & skip logic
# Time Complexity: O(2^t) where t = target, Space Complexity: O(target)

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
