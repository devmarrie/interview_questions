# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:

# Input: head = []
# Output: []

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Base case
        if not head or not head.next:
            return head
        
        #Divide the nodes recursively
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    # get the middle node
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    #Merge the sorted nodes
    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
