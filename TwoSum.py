# Problem: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

# Example
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]