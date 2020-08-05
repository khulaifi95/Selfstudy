# Reverse a linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next =None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        