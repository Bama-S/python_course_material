# set the number of days in a year as 365 in class DaysInYear.
#Change it to 366
class DaysInYear:
    def __init__(self):
        self.days = 365
    def describe(self):
        return f"days in year = {self.days}"

y = DaysInYear()
print(y.describe())
y.days = 366
print(y.describe())
