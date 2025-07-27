"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'."""

def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left = 0
        curr = 0
        vowel_sum = 0
        for right in range(len(s)):
            if s[right] in vowels:
                curr += 1
            if right-left + 1 > k:
                if s[left] in vowels:
                    curr -= 1
                left += 1
            vowel_sum = max(vowel_sum,curr)
        return vowel_sum 


# Example usage
print(maxVowels("abciiidef", 3))  # Output: 3
print(maxVowels("aeiou", 2))       # Output: 2
print(maxVowels("leetcode", 3))    # Output: 2
# Complexity Analysis
# Time Complexity: O(n), where n is the length of the string s. Each character is processed at most twice (once added and once removed).
# Space Complexity: O(1), as we are using a constant amount of space for variables.
# Note: The input string s is assumed to contain only lowercase English letters.