## Next Permutation



#### Question:

Implement next permutation, which rearranges numbers into the **lexicographically next greater permutation** of numbers.

- If such arrangement is not possible, it must rearrange it as sorted in ascending order.

- The replacement must be in-place and use only constant extra memory.



#### Example:

`1,2,3` → `1,3,2`
`3,2,1` → `1,2,3`
`1,1,5` → `1,5,1`



#### Solution:

To find the next greater permutation of array `nums`, we need to scan from the tail such that:

1. `nums[i] < nums[i+1]`, and store `i`.
2. `nums[j] > nums[i]`, and swap `nums[i]` and `nums[j]`.
3. **Reverse** the last part of the array `nums[i+1:]`.



#### Code:

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        while i >= 0 and (nums[i] >= nums[j]):
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1

            nums[i], nums[k] = nums[k], nums[i]

        n = len(nums) - 1

        while j < n:
            nums[j], nums[n] = nums[n], nums[j]
            j += 1
            n -= 1
```

