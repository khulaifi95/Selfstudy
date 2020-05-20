# Stack implementation with linked-list and resizing-array.
# LIFO


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

    def traversal(self):
        items = []
        ptr = self.first
        while ptr.item != None:
            items.append(ptr.item)
            ptr = ptr.next
        print(items[::-1])


sol = ListStackOfStrings()
sol.push('hello')
sol.push('world')
print(sol.pop())

sol.traversal()




class ArrayStackOfStrings:
    # Array implementation of a stack.
    # Resizing-array implemented for constant amortized time.

    def __init__(self, cap):
        self.array = [None] * cap
        self.len = cap

    def isEmpty(self):
        if self.array == [None]:
            return True
        return self.len == 0

    def push(self, item):
        if self.isEmpty():
            self.array[0] = item
            return
        if self.len == len(self.array):
            # repeated doubling
            self.resize(2 * len(self.array))  
        self.array[self.len] = item
        self.len += 1

    def pop(self):
        self.len -= 1
        item = self.array[self.len]
        self.array[self.len] = None
        if self.len > 0 and self.len == len(self.array) / 4:
            # halve size when array is one-quarter full
            self.resize(len(self.array) / 2)
        return item

    def size(self):
        count = 0
        for i in range(self.len):
            count += 1
        return count

    def traversal(self):
        items = []
        for i in range(self.len):
            items.append(self.array[i])
        print(items)

    def resize(self, cap):
        copy = [None] * cap
        for i in range(self.len):
            copy[i] = self.array[i]
        self.array = copy


sol2 = ArrayStackOfStrings(1)
sol2.push('hello')
sol2.push('world')
print(sol2.pop())
print(sol2.len)
sol2.traversal()