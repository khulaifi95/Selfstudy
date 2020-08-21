class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        l, r, t, b = 0, n - 1, 0, m - 1
        tot = m * n 
        res = []
        
        while tot >= 1:
            for i in range(l, r + 1):
                if tot >= 1:
                    res.append(matrix[t][i])
                    tot -= 1
            t += 1
            for i in range(t, b + 1):
                if tot >= 1:
                    res.append(matrix[i][r])
                    tot -= 1
            r -= 1
            for i in range(r, l - 1, -1):
                if tot >= 1:
                    res.append(matrix[b][i])
                    tot -= 1
            b -= 1
            for i in range(b, t - 1, -1):
                if tot >= 1:
                    res.append(matrix[i][l])
                    tot -= 1
            l += 1
        
        return res