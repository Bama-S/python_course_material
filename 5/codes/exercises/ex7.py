#Create a child class within number as integers
#demonstrate super()
class Number:
    def __init__(self,num):
        self.num = num
    def description(self):
        return f"called from parent class - the number is {self.num}"
class Integers(Number):
    def description(self,num = 1000009):
        return super().description()
        return f"called from child class - the number is {num}"#this has no effect

n1 = Number(35)
print(n1.description())
n2 = Integers(35)
print(n2.description())
