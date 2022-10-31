# set the number of days in a year as 365 in class DaysInYear. Change it to 366.
#But the output should still remain at 365
#Use Encapsulation and change the value to 366

class DaysInYear:
    def __init__(self):
        self.__days = 365
    def describe(self):
        return f"days in year = {self.__days}"
    def LeapYear(self,days):
        self.__days = days

y = DaysInYear()
print(y.describe())
y.LeapYear(366)
print(y.describe())
