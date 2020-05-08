# Reverse a linked list.

# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
