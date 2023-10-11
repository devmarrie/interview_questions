# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#     Any live cell with fewer than two live neighbors dies as if caused by under-population.
#     Any live cell with two or three live neighbors lives on to the next generation.
#     Any live cell with more than three live neighbors dies, as if by over-population.
#     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

# Example 1:

# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:

# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

from typing import List


def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        copy_board = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top = board[r-1][c] if r > 0 else 0
                dleft = board[r-1][c+1] if r > 0 and c < cols - 1 else 0
                sleft = board[r][c+1] if c < cols - 1 else 0
                dlbot = board[r+1][c+1] if r < rows - 1 and c < cols - 1 else 0
                bot = board[r+1][c] if r < rows - 1 else 0
                drbot = board[r+1][c-1] if r < rows - 1 and c > 0 else 0
                sright = board[r][c-1] if c > 0 else 0
                dright = board[r-1][c-1] if r > 0 and c > 0 else 0
                tt = top + dleft + sleft + dlbot + bot + drbot + sright + dright
                copy_board[r][c] = tt

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1 and copy_board[r][c] < 2:
                    board[r][c] = 0
                elif board[r][c] == 1 and copy_board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 1 and copy_board[r][c] == 3:
                    board[r][c] = 1
                elif board[r][c] == 1 and copy_board[r][c] > 3:
                    board[r][c] = 0
                elif board[r][c] == 0 and copy_board[r][c] == 3:
                    board[r][c] = 1