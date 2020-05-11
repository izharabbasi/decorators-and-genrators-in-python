# def num(n):
#     for i in range(1, n+1):
#         yield i


# numbers = num(10)

# for i in numbers:
#     print(i)


# for i in numbers:
#     print(i)

def even(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i


is_even = even(10)

for num in is_even:
    print(num)
