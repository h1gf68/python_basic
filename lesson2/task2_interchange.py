newList = []  # input("Введите значения элементов списка через запятую:\n").split(",")
print("Введите значения элементов списка.")
print("После каждого ввода элемента нажмите <<Enter>> для его добавления в список")
print("Для завершения ввода оставьте поле пустым и нажмите <<Enter>>")
while True:
    tmpValue = input(f"Введите {str(len(newList) + 1)}-e значение: ")
    if not tmpValue:
        break
    newList.append(tmpValue)
if len(newList) >= 2:
    print(str(newList) + " - до изменения.")
    for num in range(0, len(newList) // 2 + 1, 2):
        newList[num], newList[num + 1] = newList[num + 1], newList[num]
    print(str(newList) + " - после изменения.")
else:
    print("Невозможно выполнить задание со списком, в котором количество элементов меньше 2")
