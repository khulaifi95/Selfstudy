class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrintRecur(self, head: ListNode) -> [int]:
        # Time:  O(n)
        # Space: O(n)
        return self.reversePrintRecur(head.next) + [head.val] if head else []

    def reversePrintStack(self, head: ListNode) -> [int]:
        # Time:  O(n)
        # Space: O(n)
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]