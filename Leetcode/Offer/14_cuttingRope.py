# Cut the rope for maximum product.

class Solution:

    def cuttingRope(self, n):
        dp = [0, 1, 1]

        for i in range(3, n + 1):  # greedy for 3
            dp[i % 3] = max(max(dp[(i - 1) % 3], i - 1),
                    2 * max(dp[(i - 2) % 3], i - 2),
                    3 * max(dp[(i - 3) % 3], i - 3))
        return dp[n % 3]
