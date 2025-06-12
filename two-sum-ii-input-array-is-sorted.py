class Solution:
    def twoSum(self, numbers, target):
        # Start with two fingers: one at the beginning, one at the end
        left, right = 0, len(numbers) - 1

        # Keep going while left finger is before the right one
        while left < right:
            # Add the numbers at the left and right positions
            s = numbers[left] + numbers[right]

            if s == target:
                # If the sum matches the target, return the answer
                # Add 1 to both because the problem wants 1-based positions
                return [left + 1, right + 1]

            elif s < target:
                # If sum is too small, move left to the right to get a bigger number
                left += 1

            else:
                # If sum is too big, move right to the left to get a smaller number
                right -= 1
