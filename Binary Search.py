# Problem: https://leetcode.com/problems/binary-search/
# Approach: Classic binary search on sorted array
# Time Complexity: O(log n), Space Complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
