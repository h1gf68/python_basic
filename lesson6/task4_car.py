from random import choice


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} went."

    def stop(self):
        return f"{self.name} stopped."

    def turn(self, direction):
        return f"{self.name} turned {direction}."

    def show_speed(self):
        return f"{self.name}'s speed is {self.speed} km/h."


class TownCar(Car):
    def show_speed(self):
        return f"{self.name} was speeding!" if self.speed > 60 else Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name} was speeding!" if self.speed > 40 else Car.show_speed(self)


class SportCar(Car):
    def get_color(self):
        return f"{self.name}'s color is {self.color}"

    def show_speed(self):
        return f"Very low speed for {self.name}!" if self.speed < 60 else Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_Police=True):
        super().__init__(name, color, speed)
        self.is_police = is_Police


direction = ["right", "left", "back"]

trolleybus = TownCar("Trolleybus", "Blue", 40)
print(trolleybus.go())
print(trolleybus.show_speed())
print(trolleybus.turn(choice(direction)))
print(trolleybus.stop())
print()

bulldozer = WorkCar("Bulldozer", "Orange", 50)
print(bulldozer.go())
print(bulldozer.show_speed())
print()

lamborghini = SportCar("Lamborghini Aventador", "Red", 300)
print(lamborghini.go())
print(lamborghini.speed)
print()

dodge = PoliceCar("Dodge Charger", "White-black", 240)
print(f"{dodge.name} is police: {dodge.is_police}")
print(dodge.show_speed())
print()
