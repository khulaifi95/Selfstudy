# Linked list with cycle


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head):
        '''Determine whether a linked list has a cycle.

        Use pos to represent the position that linked to the tail. 
        This solution uses fast and slow pointers to check the cycle.

        Parameters
        ----------
        head : {[ListNode]}
        '''
        if not head:
            return head

        slow = head
        fast = head.next
        while fast and slow:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
        return False
