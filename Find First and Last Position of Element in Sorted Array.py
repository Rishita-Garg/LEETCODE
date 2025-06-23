# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Approach: Binary search twice - once for first occurrence and once for last
# Time Complexity: O(log n), Space Complexity: O(1)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [findBound(True), findBound(False)]
