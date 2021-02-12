
@timeit
def fib(n, **kwargs):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


logtime_data_2 = {}
tot = fib(20, log_time=logtime_data_2)

print(logtime_data_2)
print(timeit.func_globals)

#'func_closure', 'func_code', 
# 'func_defaults', 'func_dict', 
# 'func_doc', 'func_globals', 'func_name'