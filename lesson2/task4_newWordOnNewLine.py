while True:
    newStr = input("Введите строку из нескольких строк, разделенных пробелами:\n")
    if not newStr:  # если введенное значение пустое выходим из цикла
        break
    for num, word in enumerate(newStr.split(" "), 1):
        print(num, word[:10])
