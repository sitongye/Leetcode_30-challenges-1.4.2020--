# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example: Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        a = 0
        for i in nums:
            a = a + i
            ans = max(ans, a)
            a = max(a,0)
        return ans
        
# Note: This is implemented in Kadane's Algorithm O(n)

# within loop, number at pointer only needs to compare with the subarray with the largest sum before itself
