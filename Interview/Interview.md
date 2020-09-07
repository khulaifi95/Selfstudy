# 2020 Interview



## 1. Classical Problems





#### 1.1 Maximum Sum of Subarray

```python
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
```





#### 1.2 Merge Two Sorted Arrays

```python
class Solution:
	def merge(self, A, m, B, n):
        pa, pb = m-1, n-1
        tail = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
                
            tail -= 1
```





#### 1.3 Best Timing of Buying and Selling

```python
class Solution:
    def maxProfit(self, prices):
        minprice = int(1e9)
        maxprofit = 0
        
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
            
        return maxprofit
```





#### 1.4 Validate Palindrome String

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
                
		return True 
```





#### 1.5 Binary Tree Level Order Traversal

```python
class Solution:
	def levelOrderBFS(self, root: TreeNode) -> List[List[int]]:
    	if not root:
            return []
        res = []
        queue = [root,]
        
        while queue:
            size = len(queue)
            lvl = []
            
            for _ in range(size):
                node = queue.pop(0)
                lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(lvl)
        return res
    
    def levelOrderDFS(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        
        def dfs(index, r):
            if len(res) < index:
                res.append([])
            res[index-1].append(r.val)
            if r.left:
                dfs(index+1, r.left)
            if r.right:
                dfs(index+1, r.right)
        
        dfs(1, root)
        return res
```





#### 1.6 Copy List with Random Pointer

```python
class Solution:
	def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptr_old_list = head
        ptr_new_list = head.next
        head_old = head.next

        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next

        return head_old
```





#### 1.7 LRU Cache

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # Use fake head and fake tail.
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # Add new node to the hash table.
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
```





#### 1.8 Number of Islands

```python
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0 
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()
```





#### 1.9 Minimum Window Containing String

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





#### 1.10 Trapping Rain Water

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







## 2. Array







#### 2.1 Find Median in Sorted arrays

```python
class solution:
    def findMedianBinary(self, nums1: [int], nums2: [int]) -> float:
        # Time:  O(log(m+n))
        # Space: O(1)
        def getKthElement(k):
            pa, pb = 0, 0
            while True:
                if pa == m:
                    return nums2[pb + k - 1]
                if pb == n:
                    return nums1[pa + k - 1]
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





#### 2.2 First and Last Position

```python
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        def search(nums: [int], t: int) -> int:
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





#### 2.3 Weight of Last Stone

```python
class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        tot, n = sum(stones), len(stones)
        dp = [0 for _ in range(tot // 2 + 1)]
        for i in range(n):
            for j in range(tot // 2, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])

        return tot - 2 * dp[-1]
```





#### 2.4 Container with Most Water

```python
class Solution:
    def maxArea(self, height: [int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(area, ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return ans
```





#### 2.5 Merge Intervals

```python
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])

        return merged
```





#### 2.6 Next Permutation

```python
class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        if len(nums) <= 1:
            return

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        while i >= 0 and (nums[i] >= nums[j]):
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1

            nums[i], nums[k] = nums[k], nums[i]

        n = len(nums) - 1

        while j < n:
            nums[j], nums[n] = nums[n], nums[j]
            j += 1
            n -= 1
```





#### 2.7 Product Except Self

```python
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        n = len(nums)
        ans = [0 for i in range(n)]

        ans[0] = 1
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans
```





#### 2.8 Search in Rotated Sorted Array

```python
class Solution:
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
```





#### 2.9 Spiral Matrix

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        l, r, t, b = 0, n - 1, 0, m - 1
        tot = m * n 
        res = []
        
        while tot >= 1:
            for i in range(l, r + 1):
                if tot >= 1:
                    res.append(matrix[t][i])
                    tot -= 1
            t += 1
            for i in range(t, b + 1):
                if tot >= 1:
                    res.append(matrix[i][r])
                    tot -= 1
            r -= 1
            for i in range(r, l - 1, -1):
                if tot >= 1:
                    res.append(matrix[b][i])
                    tot -= 1
            b -= 1
            for i in range(b, t - 1, -1):
                if tot >= 1:
                    res.append(matrix[i][l])
                    tot -= 1
            l += 1
        
        return res
```





#### 2.10 Three Sum

```python
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # c as a pointer starting at tail
            c = n - 1
            target = -nums[a]

            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                # no a,b,c for b < c  
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    ans.append([nums[a], nums[b], nums[c]])

        return ans
```







## 3. Strings







#### 3.1 String Addition

```python
class Solution:
    def addStrings(self, num1: str, nums2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= or carry:
            val = carry

            if i >= 0:
                val += int(num1[i])
                i -= 1
            if j >= 0:
                val += int(num2[i])
                j -= 1

            carry, val = divmod(val, 10)
            ans = str(val) + ans

        return ans
```





#### 3.2 Most Common Word

```python
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = list(map(str, paragraph.lower().split()))

        d = defaultdict(int)
        for i in words:
            if not banned.__contains__(i):
                d[i] += 1

        return sorted(d, key=lambda x: d[x])[-1]
```





#### 3.3 Reorder Log Files

```python
class Solution:
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1, )

        return sorted(logs, key=f)
```





#### 3.4 Valid Palindrome

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda x : x == x[::-1]
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[l + 1 : r + 1]) or isPalindrome(s[l : r])

        return True
```







## 4. Lists







#### 4.1 Add Two Numbers

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        head = ptr = ListNode(None)
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            ptr.next = ListNode(s % 10)
            ptr = ptr.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
```





#### 4.2 Length of Longest Substring

```python
class Solution:
    def lenOfLongestSubstring(self, s: str) -> int:
        k, res = -1, 0
        d = {}
        for i, j in enumerate(s):
            if j in d and d[j] > k:
                k = d[j]
            d[j] = i
            res = max(res, i - k)

        return res
```





#### 4.3 Remove N-th Entry from End

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
```







## 5. Heaps







#### 5.1 Minimum Number of Meeting Rooms

```python
class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        end_p = start_p = 0

        while start_p < len(intervals):
            if start[start_p] >= end[end_p]:
                used_rooms -= 1
                end_p += 1
            used_rooms += 1
            start_p += 1

        return used_rooms
```





#### 5.2 Remove Parenthesis

```python
class Solution:
    def removeParenthesis(self, s: str) -> str:
        stack = []
        rem = set()

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            elif not stack:
                rem.add(i)
            elif c == ")":
                stack.pop()

        rem = rem.union(set(stack))

        res = []
        for i, c in enumerate(s):
            if i not in rem:
                res.append(c)

        return "".join(res)
```





#### 5.3 Top K-th Frequent Word

```python
class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```





#### 5.4 Valid Parenthesis

```python
class Solution:
    def validParenthesis(self, s: str) -> bol:
        if len(s) % 2 == 1:
            return False

        d = {")": "(", "]": "[", "}":"{", "?":"?"}
        stack = ["?"]

        for char in s:
            if char in d:
                stack.append(c)
            elif d[stack.pop()] != c:
                return False
        return len(stack) == 1
```







## 6. Hash







#### 6.1 Group Anagrams

```python
import collections

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return ans.values()

```





#### 6.2 Sum of Subarrays Equals to K

```python
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        mp = {0:1}
        count, pre = 0, 0
        for i in nums:
            pre += i
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] =mp.get(pre, 0) + 1

        return count
```





#### 6.3 Two Sum

```python
class Solution:
    def two_sum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i
```





#### 6.4 Validate Alien Dictionary

```python
class Solution:
    def validAlien(self, words: [str], order: [str]) -> bool:
        d = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if d[word1[k]] > d[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True
```







## 7. Tree







#### 7.1 Paths of Binary Tree

```python
import collections

class Solution:
    def binaryTreePathsDFS(self, root: TreeNode) -> [str]:
        # Time:  O(n^2)
        # Space: O(n^2)
        def builder(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    builder(root.left, path)
                    builder(root.right, path)

        paths = []
        builder(root, '')
        return paths
```





#### 7.2 Diameter of Binary Tree

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxd = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.maxd = max(left+right, maxd)
            return max(left, right) + 1

        depth(root)
        return self.maxd
```

####  



#### 7.3 Subtree of Another Tree

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(s, t):
            if not s and not t:
                return True
            if s and not t or not s and t or s.val != t.val:
                return False
            return check(s.left, t.left) and check(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False
            return check(s, t) or dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)
```





#### 7.4 Validate Binary Search Tree

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
```





#### 7.5 Level Order Traversal

```python
class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        res = []
        queue = deque([root,])

        while queue:
            size = len(queue)
            lvl = []

            for _ in range(size):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(lvl)

        return res
```





#### 7.6 Lowest Common Ancestor

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root
```





#### 7.7 Maximum Sum of Path

```python
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            newPath = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, newPath)

            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
```





#### 7.8 Right Side View

```python
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        # BFS
        # Time:  O(n)
        # Space: O(n)
        rval = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node:
                max_depth = max(max_depth, depth)
                rval[depth] = node.val

                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        return [rval[depth] for depth in range(max_depth + 1)]
```







## 8. Divide & Conquer







#### 8.1 Find K-th Largest Element

```python
import heapq

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heap = []
        heapify(heap)
        for i in nums:
            heappush(heap, i)
            if len(heap) > k:
                heappop(heap)

        return heap[0]

    def quickSearch(self, nums: [int], k: int) -> int:
        def partition(l, r, pivot):
            pVal = A[pivot]
            new = l
            A[pivot], A[r] = A[r], A[pivot]
            for i in range(l, r):
                if A[i] > pVal
                    A[i], A[new] = A[new], A[i]
                    new += 1
            A[new], A[right] = A[right], A[new]
            return new

        l, r = 0, len(A) - 1
        while l <= r:
            pivot = random.randint(l, r)
            new = partition(l, r, pivot)
            if new == k - 1:
                return A[new]
            elif new > k - 1:
                right = new - 1
            else:
                left = new + 1
```





#### 8.2 Merge K Lists

```python
class Solution:
    def merge2Lists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or not b:
            return a if a else b
        head = tail = ListNode()
        pa = a
        pb = b

        while pa and pb:
            if pa.val < pb.val:
                tail.next = pa
                pa = pa.next
            else:
                tail.next = pb
                pb = pb.next
            tail = tail.next

        tail.next = pa if pa else pb
        return head.next


    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        k = len(lists)
        interval = 1

        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if k > 0 else None
```





#### 8.3 Search 2D Matrix

```python
class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def search2dMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binarySearch(matrix, target, i, True)
            horizontal_found = self.binarySearch(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False
```

###### 