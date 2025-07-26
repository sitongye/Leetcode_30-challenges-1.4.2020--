# Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.

def longestSubarray(nums, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
# Time Complexity: O(n)
# Space Complexity: O(1)