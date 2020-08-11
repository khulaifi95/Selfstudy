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
The rain one location can trap is the difference between the minimum of left/ right max height and the current height.

2. **Dynamic programming**
We can save the results of maximum heights in solution **1** in arrays.
- Find the max height from current location to the left `lmax`.
- Find the max height from current location to the right `rmax`.
- Scan the two arrays and add up to the answer.

3. **Stacking DP**
We optimise the DP algorithm by adding a stack saving the boundary of the current column.
- Update the stack if current column is higher and calculate the distance to the max height `dist`.
- Find the bounded height: $bounded_height = \min(height[curr], height[stack.pop()]) - height[top])$.
- Add the trapped water to the answer: $ans += dist \times bounded_height$.

4. **Double pointers**
We notice that the height of trapped water is determined by the max height at the **lower** side.
- We can use two pointers starting from each end of the array to traverse in one sweep.

