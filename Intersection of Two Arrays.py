# 349. Intersection of Two Arrays

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Example
print(intersection([1, 2, 2, 1], [2, 2]))  # [2]
