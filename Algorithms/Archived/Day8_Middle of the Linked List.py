# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Example:
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        x = head
        i = head
        while x is not None and x.next is not None:
            x = x.next.next
            i = i.next
        return i
        
# set two pointers, the faster one moves two nodes at a time, the slower moves one at a time
# when the faster hit the end node, the slower is in the middle
