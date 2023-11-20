# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        # the node at position left
        for i in range(left - 1):
            prev, curr = curr, curr.next

        # now that we are at curr reverse the ranges
        lprev = None
        for x in range (right - left + 1):
            tmpNext = curr.next
            curr.next = lprev # curr pointer point to null or the prev node
            lprev, curr = curr, tmpNext

        #update pointers
        prev.next.next = curr
        prev.next = lprev
        return dummy.next