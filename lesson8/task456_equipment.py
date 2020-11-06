class StoreHouse:
    def __init__(self, equipDict={}):
        self.equipDict = equipDict


class Equipment:
    def __init__(self, manufacturer, model, quantity, price, discount):
        self.manufacturer = manufacturer
        self.model = model
        self.quantity = quantity
        self.price = price
        self.discount = discount


class Printer(Equipment):
    def __init__(self, manufacturer, model, quantity, price, discount, pType, paperSize):
        super().__init__(self, manufacturer, model, quantity, price, discount)
        self.pType = pType  # лазерный, струйный
        self.paperSize = paperSize  # размер бумаги


class Scanner(Equipment):
    def __init__(self, manufacturer, model, quantity, price, discount, quality):
        super().__init__(self, manufacturer, model, quantity, price, discount)
        self.quality = quality  # качество сканирования


class XeroxMachine(Equipment):
    def __init__(self, manufacturer, model, quantity, price, discount, isDocFeeder=False):
        super().__init__(self, manufacturer, model, quantity, price, discount)
        self.isDocFeeder = isDocFeeder  # качество сканирования
