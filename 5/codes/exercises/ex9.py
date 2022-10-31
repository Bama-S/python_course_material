# set the number of days in a year as 365 in class DaysInYear. Change it to 366.
#But the output should still remain at 365

class DaysInYear:
    def __init__(self):
        self.__days = 365
    def describe(self):
        return f"days in year = {self.__days}"
    

y = DaysInYear()
print(y.describe())
y.__days = 366
print(y.describe())
