## LRU Cache



#### Question:

Design and implement a data structure for **Least Recently Used** (LRU) cache. It should support the following operations: `get` and `put`.

- `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
- `put(key, value)` - Set or insert the value if the key is not already present. 
- When the cache reached its capacity, `put` should **invalidate the least recently used item** before inserting a new item.
- The cache is initialized with a **positive** capacity.



#### Example:

```C++
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```



#### Solution:

We can implement LRU cache by using **hash table with doubly-linked list** to keep all the key-value pairs in memory.

- Doubly-linked list stores pairs as the sequence of usage, where `head` key-value is most recently used, `tail` key-value is least recently used.
- Find the location in cache by hash table and move it to the `head`.
- `get` first moves the node to `head` then return the value.
- `put` creates a new key-value node if not existing, then check if LRU is **out of capacity**.

```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
    	self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:   
    # Helper functions.
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

```



We can add a **dummy head** and **dummy tail** to mark the boundaries of the list.

- Do not need to check if neighbour node exists.



#### Code:

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # Use fake head and fake tail.
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # Add new node to the hash table.
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
```

