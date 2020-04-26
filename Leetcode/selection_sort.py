
def findSmallest(arr):
    smallest, idx = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            idx = i

    return idx


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr


print(selection_sort([5, 3, 6, 2, 9, 10]))