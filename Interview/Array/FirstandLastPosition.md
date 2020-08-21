## Find First and Last Position of Elements in Sorted Array



#### Question:

Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target`.

- Your algorithm's runtime complexity must be in the order of O(log n).

- If the target is not found in the array, return [-1, -1].



#### Example:

```pseudocode
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

```pseudocode
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```



#### Solution:

Another implementation of binary search in sorted array.

We can find the first position of entry that greater than `target` and `target+1` to locate the slice of `target`.



#### Code:

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums: List[int], t: int) -> int:
            # find first position of entry >= t
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid

            return l

        a = search(nums, target)
        b = search(nums, target + 1) 
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        return [a, b - 1]
```

