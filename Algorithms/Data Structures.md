# Data Structures



### 1. Abstract data types

| Abstraction | Implementations                       |
| ----------- | ------------------------------------- |
| List        | dynamic array / linked list           |
| Queue       | linked list/ array/ stack based queue |
| Map         | tree map/ hash map/ hash table        |
| *Vehicle*   | golf cart/ bike/ motor car            |



### 2. Introduction to big-O

- Provide an upper bound of the complexity in the **worst** case.

- Quantify performance as the input size becomes **arbitrarily large**.

| **Size of input $n$** | **Big-O notation** |
| --------------------- | ------------------ |
| Constant time         | $O(1)$             |
| Logarithmic time      | $O(\log n)$        |
| Linear time           | $O(n)$             |
| Linearithmic time     | $O(n\log n)$       |
| Quadratic time        | $O(n^2)$           |
| Cubic time            | $O(n^3)$           |
| Exponential time      | $O(b^n)$, $b>1$    |
| Factorial time        | $O(n!)$            |



Generally, we have: $O(n+c) = O(n)$, $O(cn)=O(n), c >0$.

- Finding all subsets of a set - $O(2^n)$
- Finding all permutations of a sting - $O(n!)$

- Sorting using merge sort - $O(n\log n)$

- Iterating over a matrix of size $n \times m$ - $O(nm)$



### 3. Static and dynamic arrays

- Static array is a fixed length container containing $n$ elements **indexable** from the range $[0, n-1]$.

[^indexable]: Each slot and index in the array can be referenced with a number.

| **Operation** | **Static array** | **Dynamic array** |
| ------------- | ---------------- | ----------------- |
| Access        | $O(1)$           | $O(1)$            |
| Search        | $O(n)$           | $O(n)$            |
| Insertion     | N/A              | $O(n)$            |
| Appending     | N/A              | $O(1)$            |
| Deletion      | N/A              | $O(n)$            |



- Dynamic array can **grow** and **shrink** in size.

  - Implementation:

  1. Create a static array with an initial capacity.
  2. Add elements to the static array, keeping track of number of elements.
  3. If adding another element will exceed the capacity, then create a new static array with **twice** the capacity and copy all original elements into it.



### 4. Singly and doubly linked lists

- Linked list is a sequential list of nodes that hold data which point to other nodes also containing data.
  - **Node**: an object containing data and pointer(s)
  - **Head**: the first node
  - **Tail**: the last node
  - **Pointer**: reference to another node

- **Singly linked lists** only hold a reference to the next node. In the implementation, references to **head** and **tail** are maintained to the linked list.

- In a **doubly linked list**, each node holds a reference to the next and the previous node. In the implementation, references to **head** and **tail** are maintained to the linked list.

| **List**      | **Pros**                   | **Cons**                               |
| ------------- | -------------------------- | -------------------------------------- |
| Singly linked | less memory/ simple        | cannot easily access previous elements |
| Doubly linked | can be traversed backwards | takes **2x** memory                    |



- Complexity analysis
  - Removing from singly linked list: 2 pointers
  - Others: 1 pointer

| **Operation**    | **Singly linked** | **Doubly linked** |
| ---------------- | ----------------- | ----------------- |
| Search           | $O(n)$            | $O(n)$            |
| Insert at head   | $O(1)$            | $O(1)$            |
| Insert at tail   | $O(1)$            | $O(1)$            |
| Remove at head   | $O(1)$            | $O(1)$            |
| Remove at tail   | $O(n)$            | $O(1)$            |
| Remove in middle | $O(n)$            | $O(n)$            |



- Implementation methods

| clear()      | indexOf()    |
| ------------ | ------------ |
| size()       | removeTail() |
| appendTail() | remove()     |
| appendHead() | removeAt()   |
| peekHead()   | removeNum()  |
| removeHead() | contains()   |



### 5. Stack

