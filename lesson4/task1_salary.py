from sys import argv

# Введите выработку в часах, ставку в час и премию в процентах
name, hours, rate, bonus = argv

zp = float(hours) * float(rate)

print(zp + zp * float(bonus))
