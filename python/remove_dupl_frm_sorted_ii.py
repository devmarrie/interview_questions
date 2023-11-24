# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:

# Input: head = [1,1,1,2,3]
# Output: [2,3]

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                tmp = curr.next.next
                while tmp and tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                curr.next = tmp.next
            else:
                curr = curr.next
        return dummy.next