def deco_func(any_func):
    def wrp(*args, **kwargs):
        print("this is awesome")
        return any_func(*args, **kwargs)
    return wrp


@deco_func
def func1(a):
    print(f"this is function 1 {a}")


func1(2)


@deco_func
def func2(a, b):
    return a+b


print(func2(2, 3))
