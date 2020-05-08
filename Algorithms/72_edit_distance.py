# Calculate edit distance of two strings
# When same, min(left, down, left_down) + 1
# When differ, min(left, down, left_down+1) + 1

class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        
        if n * m == 0:
            return n + m
        
        # Initiate DP table
        D = [ [0] * (m + 1) for _ in range(n + 1)]  

        # Boundary
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # Recursion
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]
