"""
LeetCode #49 - Group Anagrams
Groups a list of words into sets of anagrams using character counts.
"""

def groupAnagrams(strs):
    hashmap = {}
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        key = tuple(count)
        if key not in hashmap:
            hashmap[key] = []
        hashmap[key].append(word)
    return list(hashmap.values())

# Example usage:
# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
