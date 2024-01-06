# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        if not root:
            return lst
        queue = [root]
        lr = True 

        while queue:
            level_len = len(queue)
            level_lst = []

            for _ in range (level_len):
                curr_node = queue.pop(0)
                if lr:
                    level_lst.append(curr_node.val)
                else:
                    level_lst.insert(0, curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            lst.append(level_lst)
            lr = not lr
        return lst
