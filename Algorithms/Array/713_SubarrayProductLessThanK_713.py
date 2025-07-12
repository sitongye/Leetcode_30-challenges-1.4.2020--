#Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = right = ans = 0
        product = 1
        # we need to keeo the product less than k
        for right in range(len(nums)):
            product = product * nums[right]
            while product >= k:
                product = product//nums[left]
                left += 1
            ans += right - left + 1

        return ans