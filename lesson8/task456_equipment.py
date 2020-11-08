import json


class MaxLimit(Exception):
    def __init__(self, error="This Storehouse is full!"):
        self.error = error


class StoreHouse:
    equipDict = {"Printer": [], "Scanner": [], "XeroxMachine": []}
    maxEquipment = 100  # количество мест в хранилище

    def __init__(self, devType, equipment):
        self.devType, self.equipment = devType, equipment
        self.add_equipment()

    # добавление устройства в хранилище
    def add_equipment(self):
        try:
            if self._get_count_of_equip() >= self.maxEquipment:
                raise MaxLimit()
        except MaxLimit as err:
            print(err)
        else:
            self.equipDict[self.devType].append(self.equipment)

    def send_equip(self):
        for num, devType in enumerate(self.equipDict.keys(), 1):
            print(f"{num}  {devType}")
        numType = input("What class of devices do you want to send (enter number)? : ")

        if numType.isdigit() and 0 < int(numType) <= len(self.equipDict):
            devType = list(self.equipDict.keys())[int(numType) - 1]
            countDev = StoreHouse.print_all_equip(devType)
            numDev = input("What device do you want to send (enter number)? : ")
            if numDev.isdigit() and 0 < int(numDev) <= countDev:
                countToSend = input("How many devices? : ")
                if countToSend.isdigit():
                    for _ in range(int(countToSend)):
                        self.del_equip(self, devType, self.equipDict[devType][int(numDev) - 1]["model"])
                else:
                    print("Input number! ")
            else:
                print(f"Device with number {numDev} is not exist.")
        else:
            print(f"Device with number {numType} is not exist.")

    def send_to_department(self, devType, devModel, quantity):
        for _ in range(quantity):
            if self.is_exist_equip(devType, devModel):
                self.del_equip(devType, devModel)
            else:
                print(f"Device {devType} {devModel} is not in storehouse")

    def is_exist_equip(self, devType, devModel):
        for dev in self.equipDict[devType]:
            return int(dev["quantity"]) if dev["model"] == devModel and int(dev["quantity"]) > 0 else 0

    def del_equip(self, devType, devModel):
        for dev in self.equipDict[devType]:
            if dev["model"] == devModel:
                dev["quantity"] = int(dev["quantity"]) - 1

    # количество всех устройств в хранилище
    def _get_count_of_equip(self):
        return sum([sum([int(item["quantity"]) for item in devs]) for devs in self.equipDict.values()])

    # вывод всех устройств на экран в виде таблицы
    @staticmethod
    def print_all_equip(devTypes=list(equipDict.keys())):
        countDev = 0

        def get_devices(devType):
            for device in StoreHouse.equipDict[devType]:
                nonlocal countDev
                countDev += 1
                print(f"{countDev}\t|\t{str(device)}")

        if type(devTypes) == list and len(devTypes) > 1:
            for devType in devTypes:
                print(f"----+{'-' * 120}\n\t|\t{devType}\n----+{'-' * 120}")
                get_devices(devType)
        else:
            get_devices(devTypes)
        return countDev


class Equipment:
    def __init__(self, manufacturer, model, quantity, price, discount):
        self.equipment = {"manufacturer": manufacturer, "model": model, "quantity": quantity, "price": price,
                          "discount": discount}

    def get_price(self, withDiscount=False):
        return self.equipment["price"] if not withDiscount else self.equipment["price"] * (
                1 - self.equipment["discount"])


class Printer(Equipment):
    def __init__(self, manufacturer, model, quantity, price, discount, pType):
        super().__init__(manufacturer, model, quantity, price, discount)
        self.equipment["pType"] = pType  # лазерный, струйный

        StoreHouse(type(self).__name__, self.equipment)


class Scanner(Equipment):
    def __init__(self, manufacturer, model, quantity, price, discount, quality):
        super().__init__(manufacturer, model, quantity, price, discount)
        self.equipment["quality"] = quality  # качество сканирования dpi

        StoreHouse(type(self).__name__, self.equipment)


class XeroxMachine(Equipment):
    def __init__(self, manufacturer, model, quantity, price, discount, isDocFeeder=False):
        super().__init__(manufacturer, model, quantity, price, discount)
        self.equipment["isDocFeeder"] = isDocFeeder  # есть ли автоподатчик

        StoreHouse(type(self).__name__, self.equipment)


with open("storehouse.json", encoding="utf-8") as storehouse:
    equip = json.load(storehouse)

for devType in list(equip.keys()):
    for dev in equip[devType]:
        tmp = '\",\"'.join(map(str, (list(dict(dev).values()))))
        eval(f"{devType}(\"{tmp}\")")

print("Quantity models of devices: ", StoreHouse.print_all_equip())
print()

# отправка в подразделение
StoreHouse.send_equip(StoreHouse)

print(StoreHouse.print_all_equip())
