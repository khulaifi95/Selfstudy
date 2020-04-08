# Rotate a n x n matrix by 90'.


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)  # row
        n = len(matrix[0])  # column

        for i in range(m // 2):
            for j in range(n + 1 // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

    def compose_flip(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Horizontal flip
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[
                    n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # Diagonal flip
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
