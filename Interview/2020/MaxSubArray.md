## Maximum Subarray



#### Question:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



#### Example:

```pseudocode
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```



#### Solution:

We should use **dynamic progamming** to solve optimal sub-structure problem.



1. State definition

We define the dynamic programming list `dp`, where `dp[i]` is the maximum sum of subarrays that ended with `nums[i]`.

- `dp[i]` should include `nums[i]` entry to avoid `dp[i+1]` out of bound.



2. Transfer function

If $dp[i-1]\leq 0$, we can say it contributes negatively to the sum `dp[i]`, i.e.
$$
dp[i-1] + nums[i] \leq nums[i]
$$
Thus:

- When $dp[i-1]> 0$, we let 
  $$
  dp[i] = dp[i-1] + nums[i]
  $$

- When $dp[i-1]\leq 0$, we let

$$
dp[i] = nums[i]
$$



3. Initial state

The maximum sum of array ended with `nums[0]` is itself, i.e.
$$
dp[0]=nums[0]
$$


4. Return

We return the maximum value in the `dp` list.



5. Complexity reduction

We can modify on the original array `nums` as the dynamic programming list.

- `dp[i]` is only determined by `dp[i-1]` and `nums[i]`.



#### Code:

```python
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
```

