# Queues implementation with linked-list and resizing-array.
# FIFO


class ListNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class ListQueueOfStrings:
    # List implementation of a queue.

    def __init__(self):
        self.first = ListNode(None)
        self.last = ListNode(None)

    def isEmpty(self):
        return self.first.item == None

    def enqueue(self, item):
        oldlast = self.last
        self.last = ListNode(item)
        if self.isEmpty():
            # the last is also the first when empty
            self.first = self.last
        else:
            oldlast.next = self.last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():
            # also clean up pointer to the last value
            self.last = None
        return item


sol = ListQueueOfStrings()
sol.enqueue('hello')
sol.enqueue('world')
print(sol.dequeue())
