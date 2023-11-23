# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prevNode = dummy
        count = 0

        while curr:
            count += 1
            curr = curr.next

        for i in range(count, 0, -1):
            if i == n:
                prevNode.next = prevNode.next.next
            prevNode = prevNode.next

        return dummy.next