"""
LeetCode #14 - Longest Common Prefix
Finds the longest prefix common to all strings in the list.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        ch = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]
    return strs[0]

# Example usage:
# print(longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
