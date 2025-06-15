# Problem: Daily Temperatures (Leetcode #739)
# Link: https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []  # Pair: (index, temperature)
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_index, _ = stack.pop()
                result[prev_index] = i - prev_index
            stack.append((i, temp))

        return result
