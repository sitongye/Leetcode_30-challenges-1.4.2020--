# reverse list of strings in place

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            temp = s[left_pointer]
            s[left_pointer] = s[right_pointer]
            s[right_pointer] = temp
            left_pointer += 1
            right_pointer -= 1


# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1), no additional space used