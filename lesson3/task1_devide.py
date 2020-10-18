devide = lambda d1, d2: f"{d1} / {d2} = {d1 / d2}" if d2 else "на 0 делить нельзя"


dev1 = float(input("Делимое число: "))
dev2 = float(input("Делитель: "))

print(devide(dev1, dev2))
