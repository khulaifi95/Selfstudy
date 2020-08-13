## Minimum Window String



#### Question:

Given a string `S` and a string `T`, find the minimum window in `S` which will contain all the characters in `T`.

- If there is no such window in `S` that covers all characters in `T`, return the empty string `""`.
- If there is such window, you are guaranteed that there will always be **only one unique minimum window** in `S`.



#### Example:

```pseudocode
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```



#### Solution:

We can solve this problem using a **sliding window**. 

- Move `right_ptr` to the right **until** all the characters in `t` included.
- Move `left_ptr` to the right till the constraints stand and store the `maxlen`.
- Move `right_ptr` to the right again for other solutions until the right end.

The core here is to record the amount of characters left to be found in the process.

- Use `defaultdict(int)` to count the characters in target `t` and update needed `count` in every iteration.



#### Code:

```python
from collections import defaultdict

class Solution:
    def __init__(self):
        self.ori = defaultdict(int)
        self.cnt = defaultdict(int)
    
    def isFit(self):
        for k, v in self.ori.items():
            if k not in self.cnt.keys() or v >= self.cnt[k]:
                return False
        return True      
    
    def minWindow(self, s: str, t: str) -> str:
        for i in t:
            self.ori[i] += 1
        l, r = 0, -1
        length, ansL, ansR = float('inf'), -1, -1
        sLen, tLen = len(s), len(t)
        
        while r < sLen:
            r += 1
            if r < sLen and s[r] in self.ori.keys():
                self.cnt[s[r]] += 1
            while self.isFit() and l <= r:
                if r - l + 1< length:
                    length = r - l + 1
                    ansL = l
                    ansR = l + length
                if s[l] in self.ori.keys():
                    self.cnt[s[l]] -= 1
                l += 1
        return "" if ansL == -1 else s[ansL:ansR]
        
```

