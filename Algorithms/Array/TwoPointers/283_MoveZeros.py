from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros in the array to the end while maintaining the order of non-zero elements.
        Note that you must do this in-place without making a copy of the array.
        Using two pointers to achieve this efficiently.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

# Analysis:
# Time Complexity: O(n) where n is the length of the input array
# - We traverse the array once to move non-zero elements and then fill the rest with zeros
# Space Complexity: O(1)
# - We do not use any additional data structures that scale with input size, only a few variables for indices.
# Algorithm:
# 1. Initialize a pointer to track the position of the next non-zero element.
# 2. Iterate through the array:
#    - If the current element is non-zero, place it at the position of the next non-zero element and increment the pointer.
# 3. After processing all elements, fill the remaining positions in the array with zeros.
# 4. The result is that all non-zero elements are at the front of the array, and all zeros are at the end.
# This approach ensures that the order of non-zero elements is preserved.   


# The non-zero index is used to track where the next non-zero element should go.

