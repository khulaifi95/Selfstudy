### Trapping Rain Water



#### Question:

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



#### Example:

| <img src="TrapWater.assets/Screenshot from 2020-08-09 16-52-42.png" style="zoom: 150%;" /> |
| :----------------------------------------------------------: |
|          **Fig 1**. Elevation map of trapped water           |

The above elevation map is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of rain water (blue section) are being trapped.

```pseudocode
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```



#### Solution:
1. **Brutal force**
    We directly calculate the height of water at each column.
  - Difference between the minimum of left/ right max height and the current height.

```python
def trapWater(self, height: List[int]) -> int:
    ans = 0
    size = len(height)
    for i in range(size):
        lmax = rmax = 0
        for j in range(i-1, -1, -1):
            lmax = max(lmax, height[j])
        for j in range(i, size):
            rmax = max(rmax, height[j])
        
        ans += min(lmax, rmax) - height[i]
        
    return ans  
```




2. **Dynamic programming**
   We can save the results of maximum heights in solution **1** in arrays.
   - Find the max height from current location to the left `lmax`.

```python
def trapWaterDP(self, height: List[int]) -> int:
    if height is None:
        return
    ans = 0
    size = len(height)
    lmax = rmax = [0 for i in range(size)]
    
    lmax[0] = height[0]
    for i in range(1, size):
        lmax[i] = max(height[i], lmax[i-1])
        
    rmax[size - 1] = height[size - 1]
    for i in range(size-2, -1, -1):
        rmax[i] = max(height[i], rmax[i+1])
        
    for i in range(1, size-1):
        ans += min(lmax[i], rmax[i]) - height[i]
        
    return ans
```



3. **Stacking DP**
    We optimise the DP algorithm by adding a stack saving the boundary of the current column.

  - Update the stack if current column is higher and calculate the distance to the max height `dist`.
  - Find the `bounded height:`

$$
  \text{bounded_height} = \min(height[curr], height[stack.pop()]) - height[top])
$$

  - Add the trapped water to the answer:
$$
ans += dist \times \text{bounded_height}
$$

```python
def trapWaterStack(self, height: List[int]) -> int:
    ans, curr = 0, 0
    stack = []
    while curr < len(height):
        while stack and (height[curr] > height[stack[-1]]):
            top = stack.pop()  # max height
            if not stack:
                break
            dist = curr - stack[-1] - 1
            bounded_height = min(height[curr], height[stack[-1]]) - height[top]
            ans += dist * bounded_height
        
        stack.push(curr)
        curr += 1
    
    return ans
```



4. **Double pointers**
    We notice that the height of trapped water is determined by the max height at the **lower** side.
  - We can use two pointers starting from each end of the array to traverse in one sweep.



#### Code:

```python
class Solution:
    def trapWater(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax, rmax = 0, 0
        ans = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= lmax:
                    lmax = height[left]
                else:
                    ans += lmax - height[left]
                left += 1	# update left pointer
            else:
                if height[right] >= rmax:
                    rmax = height[right]
                else:
                    ans += rmax - height[right]
                right -= 1	# update right pointer
                    
        return ans
```

