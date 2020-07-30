# Algorithms IV



## Lecture 4: Mergesort



### 1. Mergesort

#### 1.1 Process

- Divide array into two halves.
- **Recursively** sort each half.
- Merge two halves.



#### 1.2 Abstract in-place merge

**Goal**: Given two sorted subarrays `a[lo]` to `a[mid]` and `a[mid+1]` to `a[hi]`, replace with sorted subarray `a[lo]` to `a[hi]`.



#### 1.3 Merge implementation

```java
private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi)
{
  	for (int k = lo; k <= hi; k++)
      	aux[k] = a[k];	// copy
  	
  	int i = lo, j = mid+1；
    for (int k = lo; k <= hi; k++)
    {		// merge
      	if 			(i > mid)					  		a[k] = aux[j++];
      	else if (j > hi)  							a[k] = aux[i++];
      	else if (less(aux[j], aux[i]))  a[k] = aux[j++];
      	else  													a[k] = aux[i++];
    }
}
```



| ![](Mergesort.assets/Screenshot 2020-07-30 at 13.33.25.png) |
| :---------------------------------------------------------: |
|                 **Fig 4.1** Merge operation                 |



#### 1.4 Mergesort implementation

```java
public class Merge
{
  	private static void merge(...)
    {	/* as before */ }
  	
  	private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi)
    {
      	if (hi <= lo) return;
      	int mid = lo + (hi - lo) / 2;
      	sort(a, aux, lo, mid);
      	sort(a, aux, mid+1, hi);
      	merge(a, aux, lo, mid, hi);
    }
  
  	public static void sort(Comparable[] a)
    {
      	Comparable[] aux = new Comparable[a.length];
      	sort(a, aux, 0, a.length - 1);
    }
}
```



| <img src="Mergesort.assets/Screenshot 2020-07-30 at 13.33.45.png" style="zoom:100%;" /> |
| :----------------------------------------------------------: |
|               **Fig 4.2** Mergesort operation                |

