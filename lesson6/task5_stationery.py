class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def draw(self):
        return f"Запуск отрисовки ручкой фирмы \"{self.title}\""


class Pencil(Stationery):
    def draw(self):
        return f"Запуск отрисовки карандашом фирмы \"{self.title}\""


class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки маркером фирмы \"{self.title}\""

pen = Pen("Faber-Castell")
print(pen.draw())

pencil = Pencil("Erich Krause")
print(pencil.draw())

handle = Handle("Chartpak")
print(handle.draw())