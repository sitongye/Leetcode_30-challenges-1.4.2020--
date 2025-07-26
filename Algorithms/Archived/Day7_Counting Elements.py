# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.

class Solution:
    def countElements(self, arr: List[int]) -> int:
        valid = set(arr)
        i = 0
        for n in arr:
            if (n+1) in valid:
                i += 1
        return i
        
# save every elements into set, loop again to count all elements that is valid
