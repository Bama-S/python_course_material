#Create two child classes within numbers as integers and floating point
class Number:
    def __init__(self,num):
        self.num = num
class Integers(Number):
    def description(self):
        return f"{self.num} is integer"
class FloatingPoint(Number):
    def description(self):
        return f"{self.num} is floating point"

n = 45
if type(n) == int:
    n1 = Integers(n)
    print("Check the class of n1 ", type(n1))
print ("check whether n1 is an instance of FloatingPoint ", isinstance(n1,FloatingPoint))
