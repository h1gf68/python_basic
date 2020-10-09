allSeconds = int(input("Введите количество секунд: "))
if (allSeconds >= 0):
    hours = allSeconds // 3600
    minutes = (allSeconds % 3600) // 60
    seconds = (allSeconds % 3600) % 60
    print("Результат разбиения: {:02}:{:02}:{:02}".format(hours, minutes, seconds))
else:
    print("Количество секунд не может быть меньше нуля")
