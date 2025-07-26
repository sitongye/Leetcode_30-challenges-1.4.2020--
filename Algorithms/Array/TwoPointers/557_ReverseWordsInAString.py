# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = [[i for i in w] for w in s.split(" ")]
        output_lst = []
        for idx in range(len(s_lst)):
            w_lst = s_lst[idx]
            left_idx = 0
            right_idx = len(w_lst) - 1
            while left_idx < right_idx:
                temp = w_lst[left_idx]
                w_lst[left_idx] = w_lst[right_idx]
                w_lst[right_idx] = temp
                left_idx += 1
                right_idx -= 1
            output_lst.append("".join(w_lst))
        return " ".join(output_lst)
    
# time complexity: O(n)
# space complexity: O(n)