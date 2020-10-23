from math import factorial


def fact(n):
    for i in range(1, 9):
        yield factorial(i)


for el in fact(9):
    print(el)
