class Bike:
    type = "two wheeler"
    def __init__(self, model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed

A = Bike("Hero","Red","70Kmph")
B = Bike("TVS","Blue","60Kmph")
print (A.model, A.color, A.speed)
print (B.model, B.color, B.speed)
print(A.type)
#change the attributes
A.type = "three wheeler"
print(A.type)
