# Create a linked list


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def str(self):
        return self.data, self.next


k = Node(4)


class LinkedList:

    def __init__(self, head):
        self.head = head
        self.next = None

    def set_next(self, head):
        while head.next:
            self.next = head.next
            head = self.next

    def count(self):
        count = 0
        while self.head:
            self.head = self.next
            count += 1
        return count


li = LinkedList(k)