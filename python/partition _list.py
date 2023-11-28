# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummyLess = ListNode()
        currLess = dummyLess
        dummyGreat = ListNode()
        currGreat = dummyGreat
        curr = head

        while curr:
            if curr.val >= x:
                currGreat.next = curr
                currGreat = currGreat.next
            else:
                currLess.next = curr
                currLess = currLess.next
            curr = curr.next
        currLess.next = None
        currGreat.next = None

        # Merge the two
        currLess.next = dummyGreat.next
        return dummyLess.next