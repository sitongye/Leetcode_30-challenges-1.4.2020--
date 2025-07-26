class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverse only the letters in a string while keeping non-alphabetic characters in place.
        
        Time Complexity: O(n) where n is the length of the string
        - We traverse the string once with two pointers
        - Each character is visited at most once by each pointer
        
        Space Complexity: O(n) where n is the length of the string
        - We create a list to store the characters of the string
        - The list takes O(n) space
        
        Algorithm:
        1. Convert string to list for easy swapping
        2. Use two pointers from start and end
        3. Skip non-alphabetic characters on both sides
        4. Swap alphabetic characters when both pointers point to letters
        5. Continue until pointers meet
        """
        str_list = [i for i in s]
        left_pt_idx = 0
        right_pt_idx = len(str_list) - 1
        while left_pt_idx < right_pt_idx:
            while left_pt_idx < right_pt_idx and not str_list[left_pt_idx].isalpha():
                left_pt_idx += 1
            while left_pt_idx < right_pt_idx and not str_list[right_pt_idx].isalpha():
                right_pt_idx -= 1
            if left_pt_idx < right_pt_idx:
                temp = str_list[left_pt_idx]
                str_list[left_pt_idx] = str_list[right_pt_idx]
                str_list[right_pt_idx] = temp
                left_pt_idx += 1
                right_pt_idx -= 1
        return "".join(str_list)
    
