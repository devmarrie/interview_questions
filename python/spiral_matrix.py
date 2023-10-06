# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        res = []

        while l < r and t < b:
            # move left to right
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            # move from top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            if not(l < r and t < b):
                break

            # move from right to left
            for i in range(r - 1, l -1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            # move from bottom to top
            for i in range(b -1, t-1, -1):
                res.append(matrix[i][l]) 
            l += 1
        return res