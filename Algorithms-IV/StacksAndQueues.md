# Algorithms IV



## Lecture 2: Stacks and Queues



### 1. Introduction

#### 1.1 Fundamental data types

- Value: collection of objects.
- Operations: **insert**, **remove**, **iterate**, test if empty.
- Intent is clear when we insert.



#### 1.2 Difference between stack and queue

Which item to remove?

- Stack: Examine the item most recently added. (**LIFO**)
- Queue: Examine the item least recently added. (**FIFO**)



#### 1.3 Client, implementation, interface

Separate interface with implementation.

- Client cannot know details of implementation.
- Implementation cannot know details of client needs.
- Design: creates modular, reusable libraries.
- Performance: use optimised implementation where it matters.



### 2. Stacks

#### 2.1 Stack API



| public class | StackOfStrings      |                                   |
| -----------: | ------------------- | --------------------------------- |
|              | `StackOfStrings()`  | Create an empty stack.            |
|         void | `push(String item)` | Insert a new string onto stack.   |
|       String | `pop()`             | Remove and return one string.     |
|      boolean | `isEmpty()`         | Check if the stack is empty.      |
|          int | `size()`            | Return # of strings on the stack. |



#### 2.2 Linked-list representation

Maintain pointer to first node in a linked list. 

Insert/ remove from the front.

- Inner class:

#### 

```java
private class Node
{
		String item;
		Node next;
}
```

- Checker:

```java
public boolean isEmpty()
{		return first == null;	}
```



#### 2.3 Linked-list pop

- Save item to return:

```java
String item = first.item;
```

- Delete first node:

```java
first = first.next;
```

- Return saved item:

```java
return item;
```



#### 2.4 Linked-list push

- Save a link to the list:

```java
Node oldfirst = first;
```

- Create a new node at the beginning:

```java
first = new Node()
```

- Connect the new node to the old node:

```java
first.item = input;
first.next = oldfirst;
```



#### 2.5 Linked-list performance

- Every operation takes **constant** time in the worst case.
- A stack with *N* items uses $\sim 40 N$ bytes.



#### 2.6 Array representation

- Use array *s[]* to store *N* items on stack.
- `push()`: add new item at *s[N]*.
- `pop()`: remove item from *s[N-1]*.

**Defect**: Stack *overflows* when *N* exceeds capacity.



#### 2.7 Array implementation



```java
public class FixedCapacityStackOfStrings
{
  	private String[] s;
  	private int N = 0;
  
  	public FixedCapacityStackOfStrings(int capacity) // a cheat for now
    {		s = new String[capacity];	}
  
  	public boolean isEmpty()
    {		return N == 0;	}
  	
  	public void push(String item)
    {		s[N++] = item;	} // index into array then increment N
  
  	public String pop()
    {		return s[--N];	} // decrement N then index into array
}
```



#### 2.8 Stack considerations

1. **Overflow**: Use resizing array for array implementation.
2. **Underflow**: Throw exception if pop from an empty stack.
3. **Null items**: Allow null items to be inserted.
4. **Loitering**: Hold a reference to an object when no longer needed.

```java
public String pop()
{
		String item = s[--N];
		s[N] = null;
		return item;
}
```

Garbage collector can reclaim memory only if no outstanding references.



### 3. Resizing arrays

#### 3.1 How to grow array?

**First try**: Update the capacity in time.

`push()`: Increase size of array by 1.

`Pop()`: Decrease size of array by 1.

Too expensive:

- Need to copy all items to a new array.
- Inserting first *N* items takes time  $\propto 1+2+\cdots+N\sim N^2/2$.



**Solution**: If array is full, create a new array of **twice** the size, copy items.

```java
public ResizingArrayStackOfStrings()
{		s = new String[1];	}

public void push(String item)
{
  	if (N == s.length) resize(2 * s.length);
  	s[N++] = item;
}

private void resize(int capacity)
{
  	String[] copy = new String[capacity];
  for (int i = 0; i < N; i++)
  		copy[i] = s[i];
  s = copy;
}
```



#### 3.2 Amortised cost of adding to a stack

Cost of inserting first *N* items:

- *1* array access per push: *N*
- *k* array accesses to double to size *k*: *(2+4+8+...+N)*

The amortised cost is proportional to *3N*.



| <img src="StacksAndQueues.assets/Screenshot 2020-07-24 at 13.34.30.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|       **Fig 2.1** Amortised cost of adding to a stack        |



#### 3.3 How to shrink array?

**Efficient solution**:

- `push()`: Double size of array *s[]* when array is full.
- `pop()`: Halve size of array *s[]* when array is **one-quarter full**.



```java
public String pop()
{
  	String item = s[--N];
  	s[N] = null;
  	if (N > 0 && N == s.length/4) resize(s.length/2);
  	return item;
}
```

**Invaraint**: Array is between 25% and 100% full.



#### 3.4 Resizing-array performance

[^Amortised analysis]: Average running time per operation over a worst-case sequence of operations.

Starting from an empty stack, any sequence of *M* push and pop operations takes time proportional to *M*.

|           | best | worst | amortised |
| --------- | ---- | ----- | --------- |
| construct | 1    | 1     | 1         |
| push      | 1    | M     | 1         |
| pop       | 1    | M     | 1         |
| size      | 1    | 1     | 1         |



#### 3.5 Resizing-array vs. linked-list

**Linked-list**:

- Every operation takes **constant** time in the worst case.
- Uses extra time and space to deal with the links.

**Resizing-array**:

- Every operation takes constant **amortised** time.
- **Less** wasted **space**.



### 4. Queues

#### 4.1 Queue API



| public class | QueueOfStrings         |                             |
| -----------: | ---------------------- | --------------------------- |
|              | `QueueOfStrings()`     | Create an empty queue.      |
|         void | `enqueue(String item)` | Insert an item onto queue.  |
|       String | `dequeue()`            | Remove and return an item.  |
|      boolean | `isEmpty()`            | Check if the queue empty.   |
|          Int | `size()`               | Return # of items on queue. |



#### 4.2 Linked-list representation

Maintain pointers to the first and last nodes in a linked list.

Insert/ remove from opposite ends.

- Inner class:

```java
private class Node
{
		String item;
		Node next;
}
```

- Checker:

```java
public boolean isEmpty()
    {		return first == null;    }
```



#### 4.3 Linked-list enqueue

- Save a link to the last node:

```java
Node oldlast = last;
```

- Create a new node at the end:

```java
last = new Node;
last.item = input;
```

- Link the new node to the end of the list:

```java
oldlast.next = last;
```



#### 4.4 Linked-list implementation

```java
public class LinkedQueueOfStrings
{
  	private Node first, last;
  
  	private class Node
    {}
  
  	public boolean isEmpty()
    {}
  
  	public void enqueue(String item)
    {}
  
  	public String dequeue()
    {
      	String item = first.item;
      	first = first.next;
      	if (isEmpty()) last = null; // special case for empty queue
      	return item;
    }
}
```



### 4.5 Resizing-array implemtation

- Use array *q()* to store items in queue.
- `enqueue()`: add new item at *q[tail]*.
- `dequeue()`: remove item from *q[head]*.
- Update *head* and *tail* modulo the capacity.
- Add resizing array.

