class IsDigitError(Exception):
    def __init__(self, err):
        self.err = err

    @staticmethod
    def is_digit(digit):
        try:
            float(digit)
            return True
        except ValueError:
            return False


numList = []

while True:
    inpData = input("Input number: ")
    if inpData == "stop":
        print(numList)
        break

    try:
        if IsDigitError.is_digit(inpData):
            numList.append(float(inpData))
        else:
            raise IsDigitError(f"{inpData} is not number")
    except IsDigitError as err:
        print(err)
