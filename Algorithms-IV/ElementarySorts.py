
# Static
def less(a, b):
    return a < b

def exch(arr, i, j):
    swap = arr[i]
    arr[i] = arr[j]
    arr[j] = swap


# Client
arr = [9,7,5,2,3,1,4,8,6,0]


# Selection sort
# Scan from left to right.
# Invariant: 
# Entries to the left of pointer (including pointer) fixed and in ascending order.
# No entry to right of pointer is smaller than any entry to the left of pointer.

def selectionSort(a):
    N = len(a)
    for i in range(N):
        min = i
        for j in range(i+1, N):
            if less(a[j], a[min]):
                min = j
        exch(a, i, min)


# Insertion sort
# Scan from left to right.
# Invariant:
# Entries to the left of pointer (including pointer) are in ascending order.
# Entries to the right of pointer have not yet been seen.
# Partially sorted: linear

def insertionSort(a):
    N = len(a)
    for i in range(N):
        for j in range(i, 0, -1):
            if less(a[j], a[j-1]):
                exch(a, j, j-1)
            else:
                break


# Shell sort
# Use h-sorted array with decreasing strides.
# Knuth 3n+1 increment.

def shellSort(a):
    N = len(a)
    h = 1
    while h < N / 3:
        h = 3 * h + 1

    while h >= 1:
        # h-sort the array
        # print(h)
        for i in range(h,N):
            for j in range(i, h-1, -h):
                if less(a[j], a[j-h]):
                    exch(a, j, j-h)
                else:
                    break
        h = h // 3


shellSort(arr)
print(arr)

