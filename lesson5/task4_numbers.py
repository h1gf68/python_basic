my_list = ["Один", "Два", "Три", "Четыре"]

with open("task4_numbers", "r") as numbers:
    for i, line in enumerate(numbers.readlines()):
        with open("task4_numbers_new", "a") as numbers_new:
            numbers_new.write(" ".join([my_list[i], line.split()[1], line.split()[2], "\n"]))
