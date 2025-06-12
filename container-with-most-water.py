class Solution:
    def maxArea(self, height):
        # Start with two fingers: one at the beginning, one at the end
        left, right = 0, len(height) - 1

        # This keeps track of the biggest area found so far
        max_area = 0

        # Keep moving the fingers toward each other
        while left < right:
            # Find the height of the shorter line between the two
            current_height = min(height[left], height[right])

            # Calculate the width between the two lines
            width = right - left

            # Area is height * width
            current_area = current_height * width

            # Update the max_area if this one is bigger
            max_area = max(max_area, current_area)

            # Now move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1  # move left pointer to the right
            else:
                right -= 1  # move right pointer to the left

        # Return the biggest area we found
        return max_area
    