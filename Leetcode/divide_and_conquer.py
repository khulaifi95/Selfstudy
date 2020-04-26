
def sum(arr):
    n = len(arr)

    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

print(sum([2, 3, 1, 10, -5]))


def max(arr):
    n = len(arr)

    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    else:
        return arr[0] if arr[0] >= max(arr[1:]) else max(arr[1:])

print(max([2, 3, 1, 10, -5]))