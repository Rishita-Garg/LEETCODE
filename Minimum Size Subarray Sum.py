class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        LeetCode #209: Minimum Size Subarray Sum
        ----------------------------------------
        Given an array of positive integers nums and a positive integer target, 
        return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
        of which the sum is greater than or equal to target. 
        If there is no such subarray, return 0 instead.

        Example:
            Input: target = 7, nums = [2,3,1,2,4,3]
            Output: 2
            Explanation: The subarray [4,3] has the minimal length under the problem constraint.

        Approach:
        - Use sliding window with two pointers.
        - Expand right pointer until the sum ≥ target.
        - Shrink from left to minimize the window size.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
