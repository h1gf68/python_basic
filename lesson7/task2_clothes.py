from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.expenses + other.expenses

    def __str__(self):
        return self.val

    @property
    @abstractmethod
    def expenses(self):
        pass


class Coat(Clothes):
    @property
    def expenses(self):
        return round(self.val / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def expenses(self):
        return (self.val * 2 + 0.3) / 100


print(Coat(40) + Suit(240))
