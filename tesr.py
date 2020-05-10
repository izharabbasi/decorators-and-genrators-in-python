from functools import wraps
import time


def time_calc(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        print(f"this function {function.__name__} name ")
        t1 = time.time()
        retuned = function(*args, **kwargs)
        t2 = time.time()
        total = t2 - t1
        print(f"this fuction took {total} seconds ")
        return retuned
    return wrap


@time_calc
def square(a):
    return a**2


square(100000)
