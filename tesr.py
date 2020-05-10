from functools import wraps
import time


# def time_calc(function):
#     @wraps(function)
#     def wrap(*args, **kwargs):
#         print(f"this function is {function.__name__} ")
#         t1 = time.time()
#         retuned = function(*args, **kwargs)
#         t2 = time.time()
#         total = t2 - t1
#         print(f"this fuction took {total} seconds ")
#         return retuned
#     return wrap


# @time_calc
# def square(a):
#     return a**2


# print(square(100000))


def add_int(fuction):
    @wraps(fuction)
    def wrap(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return fuction(*args, **kwargs)
        else:
            print("invalid Entry")
    return wrap


@add_int
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4,[1,2,3,]))
