def my_func(val1, val2, val3):
    my_list = [val1, val2, val3]
    my_list.remove(min(val1, val2, val3))
    return sum(my_list)


# Альтернативный вариант
def my_func_another(val1, val2, val3):
    my_list = [val1, val2, val3]
    my_list.sort()
    return sum(my_list[1:])


v1, v2, v3 = input("Введите 3 числа через пробел: ").split()
print(my_func(int(v1), int(v2), int(v3)))
print(my_func_another(int(v1), int(v2), int(v3)))
