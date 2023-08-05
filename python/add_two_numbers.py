"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
     def toInt(self, head: Optional[ListNode]) -> int:
        num = 0
        curr_node = head
        while curr_node:
            num = num * 10 + curr_node.val
            curr_node = curr_node.next
        return num
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = self.toInt(l1)
        num_2 = self.toInt(l2)
        sum_int = num_1 + num_2
        
        if sum_int == 0:
            return ListNode(0)
        
        new_head = ListNode()
        final_node = new_head

        while sum_int > 0:
            last_dig = sum_int % 10
            sum_int //= 10
            final_node.next = ListNode(last_dig)
            final_node = final_node.next
        return new_head.next
    
if __name__ == '__main__':
    new_list = LinkedList()
    new_list.addTwoNumbers([3,4,2], [5,6,7])