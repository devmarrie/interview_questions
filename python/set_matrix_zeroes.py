# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
from typing import List
def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = len(matrix[0])
        rows = len(matrix)
        firstRow = False

        # Check if the first row should be zeroed
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRow = True
                break

        # Mark rows and columns that should be zeroed using the first row and first column
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out marked rows except for the first row
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        # Zero out marked columns except for the first column
        for j in range(cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if firstRow:
            for j in range(cols):
                matrix[0][j] = 0