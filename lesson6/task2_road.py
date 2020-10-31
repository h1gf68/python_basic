class Road:
    weightOneSquareMeter = 25  # kg
    thickness = 5  # cm

    def __init__(self, width, length):
        try:
            self._length = float(length)
            self._width = float(width)
        except ValueError:
            print("Hmmm, I expected other values.")

    def calculating_mass(self):
        print(f"We need {self._width * self._length * self.weightOneSquareMeter * self.thickness / 1000} tons of asphalt")


road = Road(input("Width: "), input("Length: "))
road.calculating_mass()
