class Solution:
    def removeDuplicates(self, nums):
        # If the list is empty, just return 0
        if not nums:
            return 0

        # Position to insert the next unique number
        insert_pos = 1

        # Start from the second element and check for duplicates
        for i in range(1, len(nums)):
            # If current number is different from the one before it
            if nums[i] != nums[i - 1]:
                # Put this unique number at the insert position
                nums[insert_pos] = nums[i]
                # Move insert position forward
                insert_pos += 1

        # Return the number of unique elements
        return insert_pos
