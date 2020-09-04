n= int(input())
mat = [[] for i in range(n)]
for i in range(n):
    vals = input()
    mat[i] = list(map(int, vals.split()))
    
def d(mat):
    dp = [[0 for i in range(n)] for i in range(n)]
    dp[0][0] = mat[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + mat[0][i]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + mat[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j])
            if dp[i][j-1] < dp[i-1][j]:
                dp[i][j] = dp[i][j] + abs(mat[i][j]-mat[i][j-1])
            else:
                dp[i][j] = dp[i][j] + abs(mat[i][j]-mat[i-1][j])
            
    return dp[0][0]

print(d(mat))