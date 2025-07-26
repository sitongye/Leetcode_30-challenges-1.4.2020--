# Given an array of strings, group anagrams together.
# Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            key = ''.join(sorted(list(i)))
            if key not in dic:
                dic[key] = []
            dic[key].append(i)
        output = [v for v in dic.values()]
        return output
        
        
# idea, sort the string and save them into dictionary under one key if they have the same letters.
