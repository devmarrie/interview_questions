# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:

# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lst = []

        if not root:
            return lst
        queue = [root]

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range (level_count):
                curr_node = queue.pop(0)
                level_sum += curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            level_avg = level_sum / level_count
            lst.append(level_avg)
        return lst