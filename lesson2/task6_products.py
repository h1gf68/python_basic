def isdigit(s):  # checking is int or float
    try:
        int(s)
        float(s)
        return True
    except ValueError:
        return False


products = []
product = {"name": "", "price": 0, "count": 0, "unit": ""}

print("Let's create a db of products")

while True:
    productName = price = count = unit = ""
    while True:
        if not productName:
            productName = input("Insert product's name: ")
            continue
        if not str(price) and not isdigit(price):
            price = input("Insert product's price: ")
            price = (float(price) if isdigit(price) else "")
            continue
        if not str(count) and not isdigit(count):
            count = input("Insert product's count: ")
            count = (int(count) if isdigit(count) else "")
            continue
        if not unit:
            unit = input("Insert product's unit (шт, кг, м ...): ")
            continue
        else:
            product = {"name": productName, "price": price, "count": count, "unit": unit}
            break

    products.append((len(products) + 1, product))  # add new product

    addProduct = input("Хотите добавить еще товар? (да(yes) / нет(no)): ")
    if addProduct == "да" or addProduct == "yes":
        continue
    else:
        break

"""
# для примера если лень вводить значения
products = [
    (1, {"name": "компьютер", "price": 20000, "count": 5, "unit": "шт."}),
    (2, {"name": "принтер", "price": 6000, "count": 2, "unit": "шт."}),
    (3, {"name": "сканер", "price": 2000, "count": 7, "unit": "шт."})
]
"""

analyticalTable = {"name": [], "price": [], "count": [], "unit": []}

for productItem in products:
    for key, value in productItem[1].items():
        analyticalTable[key].append(value)

for key, value in analyticalTable.items():
    print(key + "\t" + str(value) + "\n")
