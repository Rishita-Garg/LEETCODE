from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        LeetCode #239: Sliding Window Maximum
        -------------------------------------
        You are given an array of integers nums, and a sliding window of size k. 
        Return the maximum values in each sliding window.

        Example:
            Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
            Output: [3,3,5,5,6,7]

        Approach:
        - Use a deque to store indices of useful elements for current window.
        - Always keep the max element at the front of deque.
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        q = deque()  # Store indices
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if q and q[0] <= i - k:
                q.popleft()

            # Maintain elements in decreasing order in deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Append max value to result (window formed)
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
