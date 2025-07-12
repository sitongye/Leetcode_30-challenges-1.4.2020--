#Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
#For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def solution(sorted_arr, target):
    left = 0
    right = len(sorted_arr) - 1
    while left < right:
        sum = sorted_arr[left] + sorted_arr[right]
        if  sum == target:
            return True
        elif sum < target:
            left += 1
        else right -= 1
    return False



#  Time Complexity O(n)
# Space Complexity O(1) just two integers