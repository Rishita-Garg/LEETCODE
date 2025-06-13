class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        LeetCode #567: Permutation in String
        ------------------------------------
        Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
        or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.

        Example:
            Input: s1 = "ab", s2 = "eidbaooo"
            Output: true
            Explanation: s2 contains one permutation of s1 ("ba").

        Approach:
        - Use sliding window of size len(s1) over s2.
        - Compare frequency maps of s1 and current window in s2.
        Time Complexity: O(n)
        Space Complexity: O(1) — since character set is fixed (26 letters).
        """
        from collections import Counter

        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char]

            window_count[s2[i]] += 1

            if window_count == s1_count:
                return True

        return False
