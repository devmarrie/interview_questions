# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def dfs(node, depth):
            if not node:
                return 
            if depth == len(lst):
                lst.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return lst