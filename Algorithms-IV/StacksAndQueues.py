# Stacks and queues implementation.


class ListNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class ListStackOfStrings:
    # List implementation of a stack.

    def __init__(self):
        self.first = ListNode(None)

    def isEmpty(self):
        return self.first.item == None

    def push(self, item):
        # insert at the first node
        self.oldfirst = self.first
        self.first = ListNode(item)
        self.first.next = self.oldfirst

    def pop(self):
        # remove and return the first node
        item = self.first.item
        self.first = self.first.next
        return item

    def size(self):
        count = 0
        ptr = self.first
        while ptr.item != None:
            ptr = ptr.next
            count += 1
        return count

    def traverse(self):
        print(self.first.item)
        self.first = self.first.next

        ptr = self.first
        while ptr.item != None:
            print(ptr.item)
            ptr = ptr.next


sol = ListStackOfStrings()

sol.push('hello')
sol.push('world')

print(sol.size())
print(sol.isEmpty())
sol.pop()
print(sol.traverse())


class ArrayStackOfStrings:
    # Array implementation of a stack.

    def __init__(self):
        self.array = [None]
        self.len = 0

    def isEmpty(self):
        return N == 0

    def push(self, item):
        if self.len == 0:
            self.array[self.len] = item
            self.len += 1
        else:
            self.len += 1
            self.array = [None] * self.len
            self.array[self.len - 1] = item

    def pop(self):
        self.len -= 1
        return self.array[self.len]

    def size(self):
        count = 0
        for i in range(self.len):
            count += 1
        return count

sol2 = ArrayStackOfStrings()

sol2.push('hello')
sol2.push('world')

print(sol2.size())
print(sol2.pop())
# sol2.push('hi')
print(sol2.size())
print(sol2.array)
