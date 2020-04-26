import random


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

A = [random.randint(0, 20) for i in range(10)]

print(A)
print(binary_search(A, 5))
