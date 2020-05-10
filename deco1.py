def deco_func(any_func):
    def wrp():
        print("this is awesome")
        any_func()
    return wrp


@deco_func
def func1():
    print("this is function 1 ")


func1()


def func2():
    print("this is function 2 ")
