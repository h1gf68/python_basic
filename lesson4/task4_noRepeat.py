from random import randint

my_list = [randint(0, 10) for _ in range(5, 25)]
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([num for num in my_list if my_list.count(num) == 1])
