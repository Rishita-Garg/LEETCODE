# Problem: https://leetcode.com/problems/permutations/
# Approach: Backtracking with used tracking
# Time Complexity: O(n!), Space Complexity: O(n)

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res
