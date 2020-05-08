# Return the n-th element in Fibonacci.


class Solution:

    def fib(self, n):
        num = {}
        num[0] = 0
        num[1] = 1
        if n > 1:
            for i in range(2, n + 1):
                num[i] = num[i - 2] + num[i - 1]
        return int(num[n] % (1000000007))
