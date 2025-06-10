"""
LeetCode #28 - Implement strStr() using KMP Algorithm
Returns the index of the first occurrence of 'needle' in 'haystack'.
"""

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    # Step 1: Build the LPS (Longest Prefix Suffix) array for needle
    lps = [0] * len(needle)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Try the previous prefix length
            else:
                lps[i] = 0
                i += 1

    # Step 2: Use the LPS array to search in haystack
    i = j = 0  # i -> haystack, j -> needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        if j == len(needle):
            return i - j  # Match found
        elif i < len(haystack) and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1  # No match found

# Example usage:
# print(strStr("abcxabcdabxabcdabcdabcy", "abcdabcy"))  # Expected output: 15
