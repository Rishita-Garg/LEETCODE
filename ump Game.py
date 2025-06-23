# Problem: https://leetcode.com/problems/jump-game/
# Approach: Greedy - keep track of the farthest we can go
# Time Complexity: O(n), Space Complexity: O(1)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])

        return True
