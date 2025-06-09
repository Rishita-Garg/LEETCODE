# Problem: Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# Example
print(containsDuplicate([1,2,3,1]))  # Output: True
