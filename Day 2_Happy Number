# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.

# Example input: 19 output: True
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    
    def numSquareSum(self,n): 
        sq = 0
        while (n) : 
            digit = n % 10
            sq = sq + digit * digit 
            n = n // 10
        return sq
    
    def isHappy(self, n: int) -> bool:
        # create a set to store number that is visited
        s=set() 
        s.add(n) 
        # replace n until 1 is reached or be in a loop
        while True: 
          # happy number
            if n == 1: 
                return True
          # Replace n with sum of squares of digits 
            n = self.numSquareSum(n) 
          # If n is already visited, then it runs in a loop 
            if n in s: 
                return False
          # Mark n as visited 
            s.add(n) 
        return false
        
