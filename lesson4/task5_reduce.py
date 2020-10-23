from functools import reduce

print(reduce(lambda val1, val2: val1 * val2, [num for num in range(100, 1001) if num % 2 == 0]))
