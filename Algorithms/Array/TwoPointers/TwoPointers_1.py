#Example 1: Given a string s, return true if it is a palindrome, false otherwise.
#A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

def is_palindrome(s:str):
    if s == "":
        return False
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# Time Complexity O(n)
# Space Complexity O(1)