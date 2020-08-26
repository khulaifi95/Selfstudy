## Add Two Numbers with List



#### Question:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

- You may assume the two numbers do not contain any leading zero, except the number 0 itself.



#### Example:

```pseudocode
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
```



#### Solution:

We solve this problem as a simple vertical sum of two numbers.

- We first initiate the `head` for returned list.
- Set 2 pointers `p,q` on each list and iterate over `l1`, `l2`.
- Set `carry` between digits and add up with two values.
- Create new node with value `sum mod 10` to store the next digit.

Check for additional digit of 1 when result is longer than inputs.



#### Code:

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        dummy = ptr = ListNode()
        
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

