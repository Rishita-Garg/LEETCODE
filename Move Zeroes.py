# Problem: Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1

# Example
arr = [0, 1, 0, 3, 12]
moveZeroes(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]
