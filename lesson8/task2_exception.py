class MyError(Exception):
    def __init__(self, error):
        self.error = error


del1 = input("Input divisble number: ")
del2 = input("Input divider: ")

try:
    if del2 == "0":
        raise MyError("You can't divide by zero")
    print(int(del1) / int(del2))
except ValueError:
    print("Input numbers")
except MyError as err:
    print(err)
