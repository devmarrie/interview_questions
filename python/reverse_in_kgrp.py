# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0, head)
        grpPrev = dummy # for easy pointing to the next group

        while True:
            kth = self.getKthNode(grpPrev, k)
            if not kth:
                break 
            grpNext = kth.next #after k

            # now reverse the linked list
            prev, curr = kth.next, grpPrev.next
            while curr != grpNext:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp
        
            tmp = grpPrev.next
            grpPrev.next = kth
            grpPrev = tmp
        return dummy.next

    # get the group that we are trying to reverse
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr