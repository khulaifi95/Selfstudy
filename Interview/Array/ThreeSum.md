## Three Sum



#### Question:

Given an array `nums` of *n* integers, are there elements *a, b, c* in `nums` such that $a + b + c = 0$ ? Find all unique triplets in the array which gives the sum of zero.

- The solution set **must not contain duplicate triplets**.



#### Example:

```pseudocode
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```



#### Solution:

We should first **sort** the array to eliminate duplicate sets of numbers in permuted orders.

- We confine values in the solutions as: $a<b<c$. 

We try to enumerate over the list for 3 distinct values that add up to 0.

- Scan for the `first` value at the start, set a pointer for `third` value at the tail.
- Scan for the `second` value after `first`, move backward the `third` pointer if $b+c > -a$.

We can still optimise the double loop by skipping identical values in every scan.

The complexity for this solution is $O(n^2)$ for two loops.

- In the second loop, the `third` pointer moves at most *n* times, amortised to the whole loop: $O(n)/n=O(1)$.



#### Code:

```python
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            c = n - 1
            target = -nums[a]
            
            for b in range(a+1, n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    ans.append([nums[a], nums[b], nums[c]])
                    
        return ans
```

