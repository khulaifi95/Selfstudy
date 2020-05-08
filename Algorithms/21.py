# Combine two sorted lists.


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeListsRec(self, l1, l2):
        # T: O(n+m); S: O(n+m)
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeListsRec(l1.next, l2)
        else:
            l2.next = self.mergeListsRec(l1, l2.next)
            return l2

    def mergeListIter(self, l1, l2):
        # T: O(n+m), S: O(1)
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next
