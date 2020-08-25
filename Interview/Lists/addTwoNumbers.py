class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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