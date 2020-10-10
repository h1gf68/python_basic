seasons = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
while True:
    numOfMonth = input("Введите номер месяца (1-12): ")
    if not numOfMonth:  # если введенное значение пустое выходим из цикла
        break
    if numOfMonth.isdigit():  # проверка является введенное значение ли числом
        if 0 < int(numOfMonth) < 13:  # находится ли в пределах 1-12
            for season, months in seasons.items():  # для каждого сезона/ключа, месяцев/значения в словаре
                if int(numOfMonth) in months:  # находится ли введенное значение в списке месяцев
                    print(season)
