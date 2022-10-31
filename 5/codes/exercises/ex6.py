#Create two child classes within numbers as integers
#demonstrate overriding
class Number:
    def __init__(self,num):
        self.num = num
    def description(self):
        return f"called from parent class - the number is {self.num}"
class Integers(Number):
    def description(self,num = 1000009): # overrides the parent class
        return f"called from child class - the number is {num}"

n1 = Number(35)
print(n1.description())
n2 = Integers(35)
print(n2.description())
