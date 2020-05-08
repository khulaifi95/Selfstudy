class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        for _ in range(k):
            if not fast: return
            fast = fast.next  # fast goes forward k
        while fast:
            fast, slow = fast.next, slow.next  # slow and fast move together
        return slow