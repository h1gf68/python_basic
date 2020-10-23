from itertools import count, islice, cycle

my_list = [num for num in islice(count(1), 7) if num < 8]

print(my_list)
print([item for item in islice(cycle(my_list), 31)])
