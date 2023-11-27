# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        tail = head
        count = 1

        while tail.next:
            tail = tail.next
            count += 1
            

        k = k % count # to avoid redundant rotations

        if k == 0:
            return head
        
        # node before the rotating node
        curr = head
        for i in range(count - k - 1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead   