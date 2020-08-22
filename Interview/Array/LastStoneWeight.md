## Weight of Last Stone



#### Question:

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights `x` and `y` with `x <= y`.  The result of this smash is:

- If `x == y`, both stones are totally destroyed.
- If `x != y`, the stone of weight `x` is totally destroyed, and the stone of weight `y` has new weight `y-x`.

At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (or 0 if no stones left.)



#### Example:

```pseudocode
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
```



#### Solution:

For 4 stones `[a,b,c,d]`, we first pick `a,b` and get `a-b`, next we pick `c, a-b` and get `c-(a-b)= c-a+b`.

Thus the weight of the last stone can be intepreted as the **difference in weights for two piles** of stones.

We can solve the problem by finding the minimum difference in weights, i.e. each weight closest to `sum/2`.

- Knapsack problem, define `weight[i]` as the weight of stone `i`.
- Define `dp[j]` as the best choice of stones when facing `j` items, update with:

$$
dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
$$

- Return the weight of unselected stones.



#### Code:

```python
class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        tot, n = sum(stones), len(stones)
        dp = [0 for _ in range(tot // 2 + 1)]
        for i in range(n):
            for j in range(tot // 2, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])

        return tot - 2 * dp[-1]
```

