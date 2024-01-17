# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols =len(board), len(board[0])
        
        # Check the ones at the edge and mark them wwith a different xcter
        def dfs(i,j):
            if (i < 0 or i == rows or
               j < 0 or j == cols
               or board[i][j] != "O"):
               return
            board[i][j] = "T"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == "O" and 
                (i in [0, rows -1] or j in [0, cols -1])):
                   dfs(i,j)

        # Check the ones surrounded and x them
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Remark the ones at the edge wth '0's
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"

        
