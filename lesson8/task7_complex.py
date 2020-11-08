class ComplexNumber:
    def __init__(self, num):
        self.num = complex(num)

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


n1 = ComplexNumber(1 + 4j)
n2 = ComplexNumber(3 - 2j)

print(n1 + n2)
print(n1 * n2)
