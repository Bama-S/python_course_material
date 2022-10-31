#Extend the program to find the square of 1st 10 integers
class Number:
    def __init__(self,num):
        self.num = num
    def sq(self):
        self.square = self.num *self.num
        print (f"The square of {self.num} is {self.square}")
    def FirstTen():
        for i in range(1,11):
            n = Number(i)
            n.sq()

Number.FirstTen()
