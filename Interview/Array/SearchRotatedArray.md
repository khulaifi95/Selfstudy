## Search in Rotated Sorted Array



#### Question:

Given an integer array `nums` sorted in ascending order, and an integer `target`.

Suppose that `nums` is rotated at some pivot unknown to you beforehand, you should search for `target` in `nums` .

- If you found return its index, otherwise return -1.
- You should give a solution with $O(\log n)$ performance.



#### Example:

```pseudocode
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

```pseudocode
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

```pseudocode
Input: nums = [1], target = 0
Output: -1
```



#### Solution:

We should use **binary search** method to achieve $O(\log n)$ performance.

Although the array is rotated at some point, after partitioning, there always exists **one subarray that is sorted**.

We can find the sorted part and update the mid point as the new pivot for binary search process.

[^O(log n)]: We can also first find the smallest entry in the array, then use binary search in partitioned subarrays.



#### Code:

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: 	# the left side is sorted
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
```

