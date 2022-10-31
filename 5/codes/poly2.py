class Banana:
    def __init__(self,typ,color):
        self.typ = typ
        self.color = color
    def type (self):
        print(f"Banana is {self.typ}")
    def col(self):
        print(f"Banana is {self.color} in color.")
class Lemon:
    def __init__(self,typ,color):
        self.typ = typ
        self.color = color
    def type (self):
        print(f"Lemon is {self.typ}")
    def col(self):
        print(f"Lemon is {self.color} in color.")

def func(obj):
    obj.type()
    obj.col()

obj_banana = Banana("fruit","yellow")
obj_lemon = Lemon("vegetable","yellow")
func(obj_banana)
func(obj_lemon)
