## Find Median in Two Sorted Arrays



#### Question:

There are two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively. Find the median of the two sorted arrays.

- The overall run time complexity should be O(log (m+n)).
- You may assume `nums1` and `nums2` cannot be both empty.



#### Example:

```pseudocode
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

```pseudocode
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```



#### Solution:

For two sorted arrays, we have two direct methods to find the median:

- Merge two sorted arrays and return the middle location of the merged array.
- Place two pointers at the start of two arrays, move forward the pointer that related to a smaller value.

Both methods return linear performance. We can optimise the process using binary search and partitioning.

```python
def findMedianMerge(self, nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    tot = m + n
    pa, pb, pn = m - 1, n - 1, tot - 1
    aux = [0 for i in range(tot)]
    
    while pa >= 0 or pb >= 0:
        if pa == -1:
            aux[pn] = nums1[pb]
            pb -= 1
        elif pb == -1:
            aux[pn] = nums1[pa]
            pa -= 1
        elif nums1[pa] > nums2[pb]:
            aux[pn] = nums1[pa]
            pa -= 1
        else:
            aux[pn] = nums2[pb]
            pb -= 1
        
        pn -= 1
        
    if tot % 2 == 1:
        return aux[(tot - 1) // 2]
    else:
        return (aux[tot // 2] + aux[tot // 2 - 1]) / 2
            
```



1. **Binary search**

We can calculate the median by finding the *k*-th smallest number in both arrays, where *k* is either $(m+n)/2$ or $(m+n)/2+1$. 

To find the *k*-th element in two sorted arrays `A` and `B`, we compare $A[k/2-1]$ and $B[k/2-1]$ as mod division.

- If $A[k/2-1] < B[k/2-1]$, then $A[k/2-1]$ is larger than at most $k-2$ elements, which is certainly not the *k*-th smallest number. Thus we exclude $A[0:k/2-1]$ from search due to the sorted property.
- If $A[k/2-1] > B[k/2-1]$, *ditto*, we exclude $B[k/2-1]$ from search.
- If $A[k/2-1] =B[k/2-1]$, merge the equality to the first case.



| ![](FindMedian.assets/4_fig1.png) |
| :-------------------------------: |
|   **Fig 1**. Excluding elements   |



Consider following 3 bounding cases:

- If `k/2-1` element cross the boundary, we select the last element in its array and subtract `k` with # removed.
- If an array is *empty*, return the *k*-th smallest element in the other array. 
- If $k=1$, return the minimum of the first elements in two arrays.



```python
def findMedianBinary(self, nums1: List[int], nums2: List[int]) -> float:
    def getKthElement(k):
        pa, pb = 0, 0
        while True:
            if pa == m:
                return nums2[pb + k - 1]
            if pb == n:
                return nums2[pa + k - 1]
            if k == 1:
                return min(nums1[pa], nums2[pb])
            
            newpa = min(pa + k // 2 - 1, m - 1)
            newpb = min(pb + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newpa], nums2[newpb]
            if pivot1 <= pivot2:
                k -= newpa - pa + 1
                pa = newpa + 1
            else:
                k -= newpb - pb + 1
                pb = newpb + 1
    
    m, n = len(nums1), len(nums2)
    tot = m + n
    if tot % 2 == 1:
        return getKthElement((tot + 1) // 2)
    else:
        return (getKthElement(tot // 2) + getKthElement(tot // 2 + 1) / 2)
```



2. **Partitioning**

Median is the number that partitions a set into 2 equal-length subsets, where elements in one subset are always larger than those in the other.

- We first partition arrays `A` and `B` separately, and recombine the `left_part` and `right_part` in both arrays.
- When the total length `tot` is *even*, we have:

$$
len(left) = len(right) \\ \max(left) \leq \min(right) \\ median = (max(left)+min(right)) /2 
$$

- When the total length `tot` is odd, we have:

$$
len(left) = len(right+1) \\ max(left) \leq min(right) \\ median = max(left)
$$

Combing both cases for all integers, we need to ensure conditions for the cases above:

- Equal number of elements in both parts: $i + j =m-i+n-j$.
  - Induce $j = \frac {m+n+1} 2 -i$.
- No out of boundary for both arrays: $0\leq i \leq m, 0\leq j \leq n$.
  - Set `len(A)` is always smaller than `len(B)`.
- The *max* in the left part is **no larger than** the *min* in the right part: $B[j-1]\leq A[i], A[i-1] \leq B[j]$.



#### Code:

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        return self.findMedianSortedArrays(nums2, nums1)

    infty = 2**40
    m, n = len(nums1), len(nums2)
    left, right, ansi = 0, m, -1
    # max in the first half
    # min in the second half
    median1, median2 = 0, 0

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        nums_im1 = (-infty if i == 0 else nums1[i-1])
        nums_i = (infty if i == m else nums1[i])
        nums_jm1 = (-infty if j == 0 else nums2[j-1])
        nums_j = (infty if j == n else nums2[j])

        if nums_im1 <= nums_j:
            ansi = i
            median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
            left = i + 1
        else:
            right = i - 1

    return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1
```

