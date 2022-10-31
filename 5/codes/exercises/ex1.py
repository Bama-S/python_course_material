#creation of a class with number and add a method to find square
class Number:
    def __init__(self,num):
        self.num = num
        print(f"The number is {self.num}")
    def sq(self):
        self.square = self.num *self.num
        print (f"The square of {self.num} is {self.square}")

n = Number(6)
n.sq()
