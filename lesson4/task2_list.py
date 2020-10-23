my_list = list({n ** 2 for n in range(1, 10)})
new_list = []

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(my_list)

for i in range(1, len(my_list) - 1):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
print(new_list)
