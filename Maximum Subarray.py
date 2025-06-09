# Problem: Maximum Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum

# Example
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
