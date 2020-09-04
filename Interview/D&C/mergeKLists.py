class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
