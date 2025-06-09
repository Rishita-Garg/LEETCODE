# Problem: Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

# Example
print(productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]

