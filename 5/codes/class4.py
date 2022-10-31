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

class MotorBike(Bike):#Inherits parent Bike
    def sound(self, snd = "horn"):
        return super().sound(snd)
        return f"{self.model} has {snd}"


A = MotorBike("Hero","Red","70Kmph")
B = MotorBike("TVS","Blue","60Kmph")
print (A.model, A.color, A.speed)
print (B.model, B.color, B.speed)
print(A.type)
#change the attributes
A.type = "three wheeler"
print(A.type)
print(B.description())

print("Check the class of B", type(B))
print("Check whether B is an instance of PedalBike: -", isinstance(B,PedalBike))
print("Check whether B is an instance of MotorBike: -", isinstance(B,MotorBike))

print(B.sound())
print(A.sound("ringer"))#This overridess
