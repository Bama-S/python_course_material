#instance methods and added classes PedalBikem Motor Bike
#added snd method in parent
class Bike:
    type = "two wheeler"
    def __init__(self, model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed

    def description(self):
        return f"{self.model} has {self.color} color with speed of {self.speed}"

    def sound(self,snd):
        return f"{self.model} makes noise through {snd}"

class PedalBike(Bike):
    pass

class MotorBike(Bike):
    def sound(self,"horn")
    return f"{self.model} has {snd}"

A = MotorBike("Hero","Red","70Kmph")
C = PedalBike("Atlas","Blue","30Kmph")
print(A.description())
print(C.sound("Ringer"))
#print(A.sound("horn"))
#print(B.sound("ringer"))
print("Check the class of B", type(B))
print("Check whether C is an instance of PedalBike: -", isinstance(C,PedalBike))
print("Check whether C is an instance of MotorBike: -", isinstance(C,MotorBike))
