from time import strptime


class MyDate:
    def __init__(self, fdate):
        self.fdate = fdate

    @classmethod
    def get_date(cls, self):
        return str(list(map(int, self.fdate.split("-")))) if cls.is_valid(self.fdate) else "Invalid date"

    @staticmethod
    def is_valid(fdate):
        try:
            strptime(fdate, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def __str__(self):
        return self.get_date(self)


dates = ["29-02-1996", "29-02-1997", "12-13-2000", "31-04-1996", "12-05-1900", "12/05/2001"]

for fdate in dates:
    print(MyDate(fdate))
