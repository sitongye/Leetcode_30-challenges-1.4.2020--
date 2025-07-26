
# Given an array of integers nums, you start with an initial positive value startValue.

#In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

#Return the minimum positive value of startValue such that the step by step sum is never less than 1.

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [1]
        min_value = 1
        for i in range(len(nums)):
            curr = prefix[i] + nums[i]
            min_value = min(min_value, curr)
            prefix.append(curr)
        if min_value < 1:
            return 1 - min_value + 1
        else:
            return 1
        
# time complexity: O(n)
# space complexity: O(n)