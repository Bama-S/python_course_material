#instance methods and added classes PedalBikem Motor Bike


class PedalBike(Bike):
    pass

class MotorBike(Bike):#Inherits parent Bike
    pass


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
