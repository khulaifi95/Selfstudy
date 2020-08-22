## Product of Array Except Self



#### Question:

Given an array `nums` of *n* integers where $n > 1$,  return an array output such that `output[i]` is equal to the product of all the elements of nums except `nums[i]`.

- Please solve it **without division** and in time O(*n*).
- Please solve it with constant space complexity.
- The output array does not count as extra space for the purpose of space complexity analysis.



#### Example:

```pseudocode
Input:  [1,2,3,4]
Output: [24,12,8,6]
```



#### Solution:

We can use product of the left side `L` and product of the the right side `R` instead of division for the result.

To optimise the space usage, we use left side `L` as returned `ans` and build `R` in iteration.

- Build `ans` where `ans[i]` is the product of entries left to `i`.
- Build `R` in iteration and update `ans[i]` to be the total product.



#### Code:

```python
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        n = len(nums)
        ans = [0 for i in range(n)]

        ans[0] = 1
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans
```

