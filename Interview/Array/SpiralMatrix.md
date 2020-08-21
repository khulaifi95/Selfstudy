## Spiral Matrix



#### Question:

Given a positive integer `n`, generate a square matrix filled with elements from 1 to $n^2$ in spiral order.



#### Example:

```pseudocode
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```



#### Solution:

We can simulate the inward spiral filling process of a $n\times n$ matrix.

| <img src="SpiralMatrix.assets/Screenshot from 2020-08-21 15-33-06.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
| **Fig 1**. Filling up the $n\times n$ matrix in spiral order |

When the `num` is less than $n^2$, we fill the matrix from left-to-right, then top-down, then right-to-left, then bottom-up.

- Update number filled with  `num += 1`.
- Update boundaries for each side.

We use `num <= tar` as terminator because we may not fill all the cells when `n` is odd.



#### Code:

```python
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 0, n * n
        while num <= tar:
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t -= 1
            
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1
            
            for i in range(r, l - 1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            
            for i in range(b, t - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1
        
        return mat
```

