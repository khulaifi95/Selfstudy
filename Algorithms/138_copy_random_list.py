# Make a deep copy of a linked list with random pointers.


class Node:

    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head):

        if not head:  # return if head is []
            return head

        ptr = head  # set pointer on head
        
        # Creating a new weaved list of original and copied nodes.
        while ptr:
            new_node = Node(ptr.val, None, None)  # clone a new copy
            new_node.next = ptr.next  # insert into old list every other node
            ptr.next = new_node  # in cascading sequence
            ptr = new_node.next

        ptr = head  # pointer return to head

        # Link the random pointers of the new nodes created.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None  # replicate every other node
            ptr = ptr.next.next  # skip the new copy 

        # Seperate the new list from the old list.
        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_new = head.next

        while ptr_old_list:
            ptr_old_list.next = ptr_new_list.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next

        return head_new
