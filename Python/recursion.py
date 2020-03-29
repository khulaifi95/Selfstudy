
# Recursion
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError
    if n < 1:
        raise ValueError
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 500):
    print(n, ':',fibonacci(n))


# Memoisation
fibonacci_cache = {}

def fibonacci_mem(n):
    # check if n-th value is memoised
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the n-th value
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_mem(n-1) + fibonacci_mem(n-2)

    # cache the value and return
    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
    print(n, ':', fibonacci_mem(n))