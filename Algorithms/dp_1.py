# Find subsets of numbers that adds up to a total sum.
# [2, 4, 6, 10]

# Recursion


def count_sets(arr, total):
    return rec(arr, total, arr.length - 1)  # last


def rec(arr, total, i):
    """Recursive function

    Return the number of subsets which
    add up to total only up to an index.

    Arguments:
        arr {[list]} -- target array
        total {[int]} -- total sum
        i {[idx]} -- the index of an element
    """
    if total == 0:
        return 1  # {}
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        return rec(arr, total, i - 1)
    else:
        return rec(arr, total - arr[i], i - 1) +
            rec(arr, total, i - 1)


# Memoisation


def count_sets_dp(arr, total):
    mem = {}  # empty dict
    return dp(arr, total, arr.length - 1, mem)


def dp(arr, total, i, mem):
    # Big O: max = O(total * len(arr))
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = dp(arr, total, i - 1, mem)
    else:
        to_return = (dp(arr, total - arr[i], i - 1, mem) +
                     dp(arr, total, i - 1, mem))
    mem[key] = to_return
    return to_return
