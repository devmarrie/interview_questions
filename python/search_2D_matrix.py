     

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if not matrix or not matrix[0]:
            return False
        
        #Find the row containing the target
        top, bot = 0, row - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        if not (top <= bot):
            return False
        fin = (top + bot) // 2
        #now locate the target
        l, r = 0, col - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[fin][mid]:
                l = mid + 1
            elif target < matrix[fin][mid]:
                r = mid - 1
            else:
                return True
        return False