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

#### 2.1 Overview

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

#### 3.1 Overview

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



### 4. Shellsort

#### 4.1 Overview

**Idea**: Move entries more than one position at a time by *h-sorting* the array.

- An h-sorted array is *h* interleaved sorted subsequences.
- We h-sort array for **decreasing** sequence of values of *h*.



| <img src="ElementarySorts.assets/Screenshot 2020-07-24 at 08.17.56.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|         **Fig 3.2** h-sorted array as h interleaved          |



#### 4.2 H-sorting

We h-sort an array by **insertion sort**, with stride length *h*.

- Big increments $\rarr$ small subarray.
- Small increments $\rarr$ nearly in order.



| <img src="ElementarySorts.assets/Screenshot 2020-07-24 at 08.33.04.png" style="zoom:50%;" /> | <img src="ElementarySorts.assets/Screenshot 2020-07-24 at 08.33.08.png" style="zoom:50%;" /> |
| -----------------------------------------------------------: | :----------------------------------------------------------- |
|                                        **Fig 3.3** Shellsort | with increments 7,3,1                                        |



#### 4.3 Intuition

A *g*-sorted array remains *g*-sorted after *h*-sorting it.

**Increment sequence** to use:

- Powers of two: No, duplicate compares.

- $3x+1$: OK, easy to compute.
- Sedgewick: 1,5,19,41,... Good.



#### 4.4 Implementation

```Java
public class Shell
{
  	public static void sort(Comparable[] a)
    {
      	int N = a.length;
      	int h = 1;
      	while (h < N/3) h = 3*h+1; // increment sequence
      
      	while (h >= 1)
        {
          	for (int i = h; i < N; i++) // insertion sort
            {
              	for (int j = i; j >= h && 
                     less(a[j], a[j-h]); j -= h)
                  	exch(a, j, j-h);
            }
          	h = h/3; // move to next increment
        }
    }
  
  	private static boolean less(Comparable v, w)
    {}
  	private static void exch(Comparable[] a, int i, int j)
    {}
}
```



#### 4.5 Analysis

- The worst-case number of compares used by shellsort with the $3x+1$ increments is $O(N^{3/2})$.
- Number of compares used by shellsort with the $3x+1$ increments is at most by a small multiple of $N$ times number of increments used.

Actual model has not yet been discovered.



#### 4.6 Why are we interested in shellsort?

1. Example of simple idea leading to substantial performance gains.
2. Useful in practice.
   - Fast unless array size is huge.
   - Tiny fixed footprint for code.
   - Hardware sort prototype.
3. Simple algorithm, nontrivial performance, interesting questions.
   - Asymptotic growth rate?
   - Best sequence of increments?
   - Average-case performance?



### 5. Shuffling

#### 5.1 How to shuffle an array?

**Goal**: Rearrange array so that result is a **uniformly random** permutation.



#### 5.2 Shuffle sort

- Generate a random real number for each array entry.

- Sort the array.

Shuffle sort produces a uniformly random permutation of the input array, provided no duplicate values.



#### 5.3 Knuth shuffle

In iteration *i*,

- Pick integer *r* between *0* and *i* uniformly at random.
- Swap *a[i]* and *a[r]*.

**Fisher-Yates 1938**: Knuth shuffling algorithm produces a uniformly random permutation of the input array in **linear time**.



#### 5.4 Implemtation

```java
public class StdRandom
{
  	...
    public static void shuffle(Object[] a)
    {
      	int N = a.length;
      	for (int i = 0; i < N; i++)
        {
          	int r = StdRandom.uniform(i + 1); // 0 to i
          	exch(a, i, r);
        }
    }
}
```

