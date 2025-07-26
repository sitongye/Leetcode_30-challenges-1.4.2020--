#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    position = len(nums) - 1
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        position -= 1
    return result

# Time Complexity: O(n)
# Space Complexity: O(n)
# Example usage:
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
    
    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))  # Output: [4, 9, 9, 49, 121]