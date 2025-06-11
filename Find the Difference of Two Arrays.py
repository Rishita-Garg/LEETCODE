# 2215. Find the Difference of Two Arrays

def findDifference(nums1, nums2):
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

# Example
print(findDifference([1, 2, 3], [2, 4, 6]))  # [[1, 3], [4, 6]]
