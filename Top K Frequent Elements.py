# 347. Top K Frequent Elements

from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Example
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
