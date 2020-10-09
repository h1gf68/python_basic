revenue = float(input("Введите размер выручки фирмы: "))
cost = float(input("Введите размер издержек фирмы: "))

if revenue > cost:
    print("Поздравляю! Фирма принесла прибыль: {:.2f}".format(revenue - cost))
    print("Рентабельность выручки: {:.2f}%".format(revenue / cost))

    numberOfEmployees = input("Введите число работников фирмы: ")
    print("Рентабельность персонала: {:.2f} %".format((revenue - cost) / int(numberOfEmployees)))
elif revenue < cost:
    print("Фирма работает в убыток")
else:
    print("Фирма не принесла ни прибыли ни убытка")
