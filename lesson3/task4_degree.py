def degree(x, y):
    return x ** y


def degree_recursive(x, y):
    return 1 if y == 0 else (1 / x) * degree_recursive(x, y + 1)


x = float(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))

if x >= 0 and y < 0:
    print(f"{x} в степени {y} = {degree(x, y)}")
    print(f"{x} в степени {y} = {degree_recursive(x, y)}")
else:
    print("Некорректные данные")
