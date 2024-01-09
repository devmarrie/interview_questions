# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:

# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:

# Input: root = [1,0,48,null,null,12,49]
# Output: 1

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        def dfs(node):
            if not node:
                return []
        
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)
        min_val = float('inf')
        for i in range(1, len(lst)): # starting from the second val onwards
            min_val = min(min_val, lst[i] - lst[i-1])
        return min_val
 