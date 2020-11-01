class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return str(self.cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, count):
        return Cell("".join(["*" * count + "\n" for _ in range(self.cells // count)]) + "*"*(self.cells % count))


c1 = Cell(14)
c2 = Cell(12)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 // c2)
print()
print(c1.make_order(4))

