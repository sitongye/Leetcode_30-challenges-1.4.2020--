"""Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing. Return the resulting string."""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        str_arr = [i for i in word]
        j = 0
        for idx in range(len(str_arr)):
            if str_arr[idx] == ch:
                # reverse
                while j<idx:
                    temp = str_arr[j]
                    str_arr[j] = str_arr[idx]
                    str_arr[idx] = temp
                    j += 1
                    idx -= 1
                return "".join(str_arr)
        return "".join(str_arr)
    
# Time Complexity: O(n) where n is the length of the string
# - We traverse the string once to find the character and then reverse the prefix.
# Space Complexity: O(n) where n is the length of the string
# - We create a list to store the characters of the string. 