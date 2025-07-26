from matplotlib.pylab import integer

"""
209. Minimum Size Subarray Sum
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Using a sliding window approach, we can efficiently find the minimal length of the subarray."""

def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0