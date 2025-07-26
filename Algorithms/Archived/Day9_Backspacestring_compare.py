# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.



class Solution: 
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ans
        return process(S)==process(T)
