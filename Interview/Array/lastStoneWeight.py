class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        tot, n = sum(stones), len(stones)
        dp = [0 for _ in range(tot // 2 + 1)]
        for i in range(n):
            for j in range(tot // 2, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])

        return tot - 2 * dp[-1]