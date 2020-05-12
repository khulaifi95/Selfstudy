
# # Game of life

# # i = 1:
# # n < 2: i -> 0
# # n = 2 or n = 3: /
# # n > 3: -> 0
# #
# # i = 0:
# # n = 5: i -> 1

import numpy as np


class Solution:

    def conv(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])

        board_exp = np.pad(board, 1, 'constant')  # zero padding
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # kernel

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1
        return board

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Replace 1->0 with -1, 0->1 with 2.
        """

        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                     (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):

                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1

                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
