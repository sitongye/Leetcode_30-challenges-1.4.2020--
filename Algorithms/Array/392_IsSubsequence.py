# https://leetcode.com/problems/is-subsequence/
#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

def is_subsequence(s,t):
    if not s:
        return True
    if not t:
        return False
    
    s_index = 0
    t_index = 0
    
    while t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
            if s_index == len(s):
                return True
        t_index += 1
    
    return False

# Time Complexity: O(n), where n is the length of t
# Space Complexity: O(1), no additional space used
# Example usage:
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(is_subsequence(s, t))  # Output: True

    s = "axc"
    t = "ahbgdc"
    print(is_subsequence(s, t))  # Output: False