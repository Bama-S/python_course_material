#Add two numbers to find the square
class Number:
    def __init__(self,num):
        self.num = num
    def sq(self):
        self.square = self.num *self.num
        print (f"The square of {self.num} is {self.square}")

n = Number(6)
n.sq()
n = Number(7)
n.sq()
