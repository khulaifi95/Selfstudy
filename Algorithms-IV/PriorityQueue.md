# Algorithms IV



## Lecture 6: Priority Queues



### 1. Introduction

#### 1.1 Collections

A `collection` is a data type that stores a group of items.

```

```



| data type      | core operations             | data structure                 |
| -------------- | --------------------------- | ------------------------------ |
| stack          | `push`, `pop`               | linked list, resizing array    |
| queue          | `enqueue`, `dequeue`        | linked list, resizing array    |
| priority queue | `insert`, `delete-max`      | binary heap                    |
| symbol table   | `put`, `get`, `delete`      | binary search tree, hash table |
| set            | `add`, `contains`, `delete` | binary search tree, hash table |



#### 1.2 Priority queue

Deletion of items for every type of collection:

- Stack: Remove the item most recently added.
- Queue: Remove the item least recently added.
- Randomised queue: Remove a random item.

Priority queue removes the **largest/ smallest** item.



#### 1.3 API

Items are required to be generic and `Comparable`.

| public class | MaxPQ            | <Key extends Comparable<key>>        |
| ------------ | ---------------- | ------------------------------------ |
|              | `MaxPQ()`        | Create an empty priority queue.      |
|              | `MaxPQ(Key[] a)` | Create with given keys.              |
| void         | `insert(Key v)`  | Insert a key into priority queue.    |
| Key          | `delMax()`       | Return and remove a largest key.     |
| boolean      | `isEmpty()`      | Check if the priority is empty.      |
| Key          | `max()`          | Return a largest key.                |
| int          | `size()`         | Number of entries in priority queue. |



#### 1.4 Applications

Priority queues are widely used in the following applications:

- Event-driven simulation, e.g. colliding particles.
- Numerical computation, e.g. reducing round-off.
- Discrete optimisation, e.g. scheduling.
- Artificial intelligence, e.g. A* search.
- Operating systems, e.g. load balancing.
- Data compression, e.g. Huffman codes.
- Graph searching, e.g. Dijkstra's algorithm.
- Number theory, e.g. sum of powers.
- Statistics, e.g. Bayesian spam filter.



#### 1.5 Client

**Goal**: Find the largest *m* items in a stream of *n* (**huge**) items.

**Constraint**: Not enough space to store the whole *n* items.



| implementation | time      | space |
| -------------- | --------- | ----- |
| sort           | $n\log n$ | *n*   |
| elementary PQ  | $mn$      | *m*   |
| binary heap    | $n\log m$ | *m*   |
| best in theory | *n*       | *m*   |



#### 1.6 Ordered and unordered array implementation

 We need to implement **all** operations efficiently.



| implementation  | insert   | delete max | max      |
| :-------------- | -------- | ---------- | -------- |
| unordered array | 1        | n          | n        |
| ordered array   | n        | 1          | 1        |
| goal            | $\log n$ | $\log n$   | $\log n$ |

We need to find a solution of **partially-ordered array**.



### 2. Binary heaps

#### 2.1 Complete binary tree

A binary tree consists of empty or node with links to left and right binary trees.

A complete tree is **perfectly balanced**, except for bottom level.

- The height of a complete binary tree with *n* nodes is $\lg n$.



#### 2.2 Representation

Binary heap is array representation of a heap-ordered complete binary tree.

- Heap-ordered binary tree:
  - Keys in nodes.
  - Parent's key no smaller than children's key.
- Array representation:
  - Indices start at 1.
  - Take nodes in **level order**.
  - No explicit links needed.



#### 2.3 Properties

- The largest key in `a[1]`, which is the **root** of binary tree.
- We can use array indices to move through tree.
  - Parent of node at *k* is at *k/2*.
  - Children of node at *k* are at *2k* and *2k+1*.



| <img src="PriorityQueue.assets/Screenshot from 2020-08-04 15-02-04.png" style="zoom:80%;" /> |
| :----------------------------------------------------------: |
|               **Fig 6.1** Heap representations               |



#### 2.4 Basic operations

- `Insert`: Add node at the end, then **swim it up**, $\leq 1+\lg n$ compares.

```java
public void insert(Key x)
{	
	pq[++n] = x;
	swim(n);
}
```

- `Remove max`: Exchange root with node at end, then **sink it down**, $\leq 2\lg n$ compares.

```java
public void delMax()
{
	Key max = pq[1];
	exch(1, n--);
	sink(1);
	pq[n+1] = null;	// prevent loitering
	return max;
}
```



#### 2.5 Promotion

When a key is *larger* than its parent's key, **promote** it to eliminate the violation.

- `Exchange` key in child with key in parent.
- Repeat until heap order restored.

```java
private void swim(int k)
{
    while (k > 1 && less(k/2, k))
    {
        exch(k, k/2);
        k = k/2;
    }
}
```



#### 2.6 Demotion

When a key is *smaller* than one or both of its children's, **demote** to eliminate the violation.

-  `Exchange` key in parent with key in **the larger child**.
- Repeat until heap order restored.

```java
private void sink(int k)	//reheapify
{
    while (2*k <= n)
    {
        int j = 2*k;
        if (j < n && less(j, j+1)) j++;
        if (!less(k, j))	break;
        exch(k, j);
        k = j;
    }
}
```



#### 2.7 Full implementation

```java
public class MaxPQ<key extends Comparable<Key>>
{
    private Key[] pq;
    private int n;
    
    // fixed capacity builder
    public MaxPQ(int capacity)
    {	pq = (Key[]) new Comparable[capacity+1];	}
    
    // PQ operations
    public boolean isEmpty()
    {	return n == 0;	}
    public void insert(Key key);
    public Key delMax();
    
    // heap helper functions
    private void swim(int k);
    private void sink(int k);
    
    // array helper functions
    private boolean less(int i, int j)
    {	return pq[i].compareTo(pq[j]) < 0};
    private void exch(int i, int j)
    {	Key t = pq[i]; pq[i] = pq[j]; pq[j] = t;}
}
```



#### 2.8 Implementation cost

Binary heap returns **logarithmic** cost for `insert` and `del_max` operations.

