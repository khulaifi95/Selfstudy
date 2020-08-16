## Container with Most Water



#### Question:

Given *n* non-negative integers $a_1, a_2, \cdots, a_n$ , where each represents a point at coordinate $(i, a_i)$. *n* vertical lines are drawn such that the two endpoints of line *i* is at $(i, a_i)$ and $(i, 0)$. Find two lines, which together with x-axis forms a container, such that the container contains the most water.

- You may not slant the container and n is at least 2.



#### Example:

| <img src="ContainerWithMostWater.assets/question_11.jpg" style="zoom:80%;" /> |
| :----------------------------------------------------------: |
|          **Fig 1**. Find container with most water           |



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



#### Solution:

We can solve this problem using two pointers `l` and `r` from both ends of the height.

- The area of water contained is calculated as `area = min(height[l], height[r])*(r-l)`.

- For two locations in the height array, if `height[l] < height[r]`,  we should move the pointer that relates to the smaller value, otherwise `min(height[l'], height[r]) <= min(height[l], height[r])`.
- Keep updating the maximum of the area and return `ans`.



#### Code:

```python
from typing import List
class Solution:
    def(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
       
        return ans
```

