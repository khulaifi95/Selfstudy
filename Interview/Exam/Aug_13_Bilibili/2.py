import math

def isPrime(n):
    if n < 2:
        return
    for i in range(2, int(math.sqrt(n))+1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    prime = []
    for i in range(n):
        if isPrime(i):
            prime.append(i)

    ans = 0
    lo = 0, hi = 1
    while lo < hi:
        while sum(prime[lo:hi+1]) < n:
            hi += 1
        if sum(prime[lo:hi+1]) == n:
            ans += 1
            lo -= 1

    return ans

