import time
from functools import wraps
def time_calculator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Executing.......{func.__name__}")
        t1=time.time()
        returned_value=func(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        return total_time
    return wrapper


@time_calculator
def func(n):
    l=[i**2 for i in range(1,n+1)]
    return l

print(func(100000000))