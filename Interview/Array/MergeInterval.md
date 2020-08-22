## Merge Intervals



#### Question:

Given a collection of intervals, merge all overlapping intervals.



#### Example:

```pseudocode
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

```pseudocode
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```



#### Solution:

We first need to sort the intervals by their left boundary: `intervals.sort(key=lambda x: x[0])`.

- If the left point of current interval is larger than the right point of `merged` intervals, we add it to the last position.
- Otherwise, we update the right point of last interval: `merged[-1][1] = max(merged[-1][1], interval[1])`.



#### Code:

```python
class Solution:
    def merge(self, interval: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for i in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
```

