# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:

# Input: root = []
# Output: 0

# Example 3:

# Input: root = [1]
# Output: 1

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:

#         def dfs(node):
#             if  not node:
#                 return 0
#             return dfs(node.left) + dfs(node.right) + 1
#         return dfs(root)

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # calculate left and right heights
        def lheight(node):
            if  not node:
                return 0
            return lheight(node.left) + 1
        
        def rheight(node):
            if  not node:
                return 0
            return rheight(node.right) + 1
        
        #compare the heights and find tt if complete and balanced
        l, r = lheight(root), rheight(root)
        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return (2**l) - 1
