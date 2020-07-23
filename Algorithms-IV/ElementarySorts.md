# Algorithms-IV



## Lecture 3. Elementary Sorts



### 1. Rules

#### 1.1 Sorting problem

Rearranges array of items into ascending/descending order with keys as a part of the item.



#### 1.2 Callbacks

**Goal**:  to sort any type of data.

Callback provides **references** to executable codes for different types.

- Client passes array of objects to `sort()` function.
- The `sort()` function calls back object's `compareTo()` method as needed.

**Implementation** of callbacks:

- Java: comparable interfaces.
- C++: class-type functors.
- Python: first-class functions.



#### 1.3 Total order

A total order is a binary relation $\leq$ that satisfies:

- Antisymmetry: if *v* ≤ *w* and *w* ≤ *v*, then *v* = *w*. 
- Transitivity: if *v* ≤ *w* and *w* ≤ *x*, then *v* ≤ *x*. 
- Totality: either *v* ≤ *w* or *w* ≤ *v* or both.



#### 1.4 Two useful sorting abstractions

Two essential **helper functions** refer to data through compares and exchanges.

1. **Less**: Is item *v* less than *w*?

```java
private static boolean less(Comparable v, Comparable w)
{  return v.compareTo(w) < 0;  }
```



2. **Exchange**: Swap items in array *a[ ]* at index *i* with the one at index *j*.

```Java
private static void exch(Comparable[] a, int i, int j)
{
		Comparable swap = a[i];
		a[i] = a[j];
		a[j] = swap;
}
```



#### 1.5 Testing

**Goal**: test if an array is sorted.

```Java
private static boolean isSorted(Comparable[] a)
{
		for (int i = 1; i < a.length; i++)
				if (less(a[i], a[i-1])) return false;
    return true;
}
```



### 2. Selection sort

#### 2.1 Process

In iteration *i*, 

- Find index *min* of the smallest **remaining** entry.

- Swap *a[i]* and *a[min]*.



#### 2.2 Invaraints

The pointer $\uarr$ always scans from left to right.

- Entries on the left of (including) $\uarr$ are fixed and in ascending order.
- No entry to the right of $\uarr$ is smaller than any entry to the left of $\uarr$.



#### 2.3 Inner loop

To maintain algorithm invariants,

- Move the pointer to the right:

```Java
int N = a.length;
for (int i = 0; i < N; i++) {}
```

- Identify index of minimum entry on the right:

```Java
int min = i;
for (int j = i+1; j < N; j++)
		if (less(a[j],a[min]))
				min = j;
```

- Exchange into position:

```Java
exch(a, i, min);
```



#### 2.4 Analysis

Selection sort uses $(N-1)+(N-2)+\dots+1+0\sim N^2/2$ compares and *N* exchanges.

- Running time is insensitive to input: **quadratic**, even if input sorted.

- Data movement is minimal: **linear**.



### 3. Insertion sort

#### 3.1 Process

In iteration *i*,

- Swap *a[i]* with each larger entry to its left.



#### 3.2 Invariants

The pointer $\uarr$ scans from left to right.

- Entries to the left of (including) $\uarr$ are in ascending order.
- Entries to the right of $\uarr$ have not yet been seen.



#### 3.3 Inner loop

To maintain algorithm invariants,

- Move the pointer to the right:

```java
int N = a.length;
for (int i = 0; i < N; i++) {}
```

- Moving from right to left, exchange *a[i]* with each larger entry to the left:

```Java
for (int j = i; j > 0; j--)
		if (less(a[j] < a[j-1]))
				exch(a, j, j-1);
    else break;
```



#### 3.4 Analysis

To sort a randomly-ordered array with distinct keys, insertion sort uses $\sim 1/4N^2$ compares and $\sim 1/4 N^2$ exchanges on average.

- Expect each entry to move halfway back.



| <img src="ElementarySorts.assets/Screenshot 2020-07-22 at 10.45.00.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|             **Fig 3.1** Trace of Insertion Sort              |



#### 3.5 Best and worst cases

- **Best case**: 

  If the array is in ascending order, insertion sort makes $N-1$ compares and *0* exchanges.

- **Worst case**:

  If the array is in descending order without duplicates, insertion sort makes $\sim 1/2N^2$ compares and $\sim 1/2N^2$ exchanges.



#### 3.6 Partially-sorted arrays

An **inversion** is a pair of keys that are out of order.
$$
A \ E \ E \ L \ M \ O \ T \ R \ X \ P \ S  \\ \text{T-P, T-R, R-P}
$$
An array is **partially-sorted** if the number of inversions is less than $cN$.
$$
Sorted(N) + Random(10)
$$
For partially-sorted arrays, insertion sort runs in **linear time**.

- Number of exchanges equals the number of inversions.

$$
\text{No. compares} = \text {No. inversions} + (N-1)
$$

