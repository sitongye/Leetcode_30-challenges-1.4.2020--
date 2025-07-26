"""You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part."""
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg_lst = [-1] * n
        prefixes = [nums[0]]
        for i in range(1, len(nums)):
            prefixes.append(prefixes[-1] + nums[i])
        for i in range(k,n-k):
            minus = (prefixes[i+k] - prefixes[i-k] + nums[i-k])
            avg_lst[i] = int(minus//(2*k+1))
        return avg_lst
    
# time complexity: O(n)
# space complexity: O(n)
        
        