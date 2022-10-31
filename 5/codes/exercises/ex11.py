#Have two classes integers and floats. Have a same function of cube and demonstrate
#through polymorphism

class Integers:
    def __init__(self,num):
        self.num = num

    def cube(self):
        self.cb = (self.num)**3
        return f"Cube of {self.num} is {self.cb}"

class FloatingPoint:
    def __init__(self,num):
        self.num = num

    def cube(self):
        self.cb = (self.num)**3
        return f"Cube of {self.num} is {self.cb}"

n1 = Integers(5)
n2 = FloatingPoint(5.5)
print(n1.cube())
print(n2.cube())
