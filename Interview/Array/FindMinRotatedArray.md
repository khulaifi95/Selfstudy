## Find Minimum in Rotated Sorted Array



#### Question:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you. Find the minimum element.

- `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`.
- The array may **contain duplicates**.



#### Example:

```pseudocode
Input: [1,3,5]
Output: 1
```

```pseudocode
Input: [2,2,2,0,1]
Output: 0
```



#### Solution:

We should use binary search method to solve the problem of finding smallest entry in a sorted array.

An ascending array with duplicates after rotation can be visualised as:

| <img src="FindMinRotatedArray.assets/Screenshot from 2020-08-21 14-38-06.png" style="zoom: 50%;" /> |
| :----------------------------------------------------------: |
|      **Fig 1**. Visualisation of a rotated sorted array      |

**Invariant**: The last entry is always `>=` entries on the right of the `min`,  `<=` entries on the left of the `min`.

We can thus find the `min` using two boundaries `low` and `high`, and comparing `nums[pivot]` with `nums[high]`.

- $nums[pivot]<nums[high]$: `pivot` on the right of `min`, ignore the right partition.
- $nums[pivot]> nums[high]$: `pivot` on the left of `min`, ignore the left partition.
- $nums[pivot] = nums[high]$: Duplicates make it impossible to infer, move `high` one step to the left. 



| <img src="FindMinRotatedArray.assets/Screenshot from 2020-08-21 14-46-06.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|          **Fig 2**. When nums[pivot] == nums[high]           |



#### Code:

```python
class Solution:
	def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            if nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
                
        return nums[low]
```

