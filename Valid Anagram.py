"""
LeetCode #242 - Valid Anagram
Checks if two strings are anagrams of each other without using built-in libraries.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26  # Assuming only lowercase English letters
    for ch in s:
        count[ord(ch) - ord('a')] += 1
    for ch in t:
        count[ord(ch) - ord('a')] -= 1
    for c in count:
        if c != 0:
            return False
    return True

# Example usage:
# print(isAnagram("anagram", "nagaram"))  # True
