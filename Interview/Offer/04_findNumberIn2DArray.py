
# Find a number in an increment 2D array.

# Input: matrix, number
# Return: True or False


class Solution:

    def brutal(self, matrix, target):
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
                    break
        return False

    def iteration(self, matrix, target):
        n = len(matrix) - 1
        m = 0
        while n >= 0 and m < len(matrix[0]):
            if target < matrix[n][m]:
                n -= 1
            elif target > matrix[n][m]:
                m += 1
            else:
                return True
