def climbStairs(n):
    # write code here
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(3,n+1):
            dp[i-1] = dp[i-2] + dp[i-3]
    return dp[n-1]    

print(climbStairs(5))