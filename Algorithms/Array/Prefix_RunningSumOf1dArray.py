# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = [nums[0]]
        if len(nums) == 1:
            return runningsum
        for i in range(1, len(nums)):
            runningsum.append(runningsum[i-1] + nums[i])
        return runningsum
    

# time complexity: O(n)
# space complexity: O(n)
# where n is the length of the input array nums.