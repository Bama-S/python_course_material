#Create a child classes within number as integers
#demonstrate inheritance
class Number:
    def __init__(self,num):
        self.num = num
class Integers(Number):
    def double(self):
        self.twice = self.num*2
        return f"{self.twice} is double of {self.num}"
n = Integers(45)
print(n.double())
