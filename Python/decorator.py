import time

logtime_data = {}

def timeit(method, log_data=logtime_data):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        name = method.__name__.upper()
        log_data.update({name:(te - ts)})
        return result

    return timed


def memoize(f):
    memo = {}
    def getter(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return getter


class Memoize:
    
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)

        return self.memo[args]


@timeit
def get_all_employee_details(**kwargs):
    print('employee details')

@timeit
def recsum(num, **kwargs):
    if num == 1:
        return 1
    return num + recsum(num-1)

@timeit
def tail_recsum(num, running_total=0, **kwargs):
    if num == 0:
        return running_total
    return tail_recsum(num - 1, running_total + num)

@Memoize
@timeit
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@Memoize
@timeit
def tail_fib(n, running_total=0):
    if n==0:
        return running_total
    elif n==1:
        return running_total + 1
    else:
        return tail_fib(n-1, running_total + n-1) + tail_fib(n-2, running_total + n)

# employees = get_all_employee_details(log_time=logtime_data)
# sum = recsum(100, log_time=logtime_data)
# tail_sum = tailrecsum(100, log_time=logtime_data)
tot_1 = fib(100)
tot_2 = tail_fib(100)
print(tot_1)
print(tot_2)
print(logtime_data)