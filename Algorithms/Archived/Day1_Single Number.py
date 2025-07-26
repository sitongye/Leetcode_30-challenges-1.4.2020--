# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# requirement: linear runtime complexity

# example input:[2,2,1] output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x = x^i
        return x

# This is a XOR solution, any number with an xor with itself results in 0, thus, number with two occurence will be zero after XOR,
#any number with zero with be itself after XOR, thus the return will be that number after operating XOR on the whole sequence 
