# 350. Intersection of Two Arrays II

from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result

# Example
print(intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
