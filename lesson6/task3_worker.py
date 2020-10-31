class Worker:
    _income = {"wage": 60000, "bonus": 0.3}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        return f"Worker's name is {self.name} {self.surname}"

    def get_total_income(self):
        income = Worker._income
        return f"{self.name} earns {income['wage'] + income['wage'] * income['bonus']} $"


worker1 = Position("Mark", "Harvick", "engineer")
print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker1.name, worker1.surname)
