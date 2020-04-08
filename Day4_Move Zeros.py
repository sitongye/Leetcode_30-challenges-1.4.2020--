# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example: Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# requirment: 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.



# My Implementation:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        c=0
        while i!=len(nums):
            if nums[i] == 0:
                c += 1
                nums.pop(i)
            else:
                i=i+1
        for n in range(c):
            nums.append(0)
 # The idea is to pop zero when zero is detected and add to count, and append number of zeros at the end
 
