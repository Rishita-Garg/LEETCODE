# Problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Approach: Binary search to find the peak where A[i] > A[i+1]
# Time Complexity: O(log n), Space Complexity: O(1)

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
