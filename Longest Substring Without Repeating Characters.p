class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LeetCode #3: Longest Substring Without Repeating Characters
        -----------------------------------------------------------
        Given a string s, find the length of the longest substring 
        without repeating characters.

        Example:
            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3.

        Approach:
        - Use sliding window and a set to track unique characters.
        - Move the window right until a duplicate is found.
        - Remove the leftmost character until the window is unique again.
        - Keep track of max window size.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        left = max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
