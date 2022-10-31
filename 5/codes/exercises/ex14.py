#Have a class bird and add a class method
class Bird:
    def __init__(self, name,color):
        self.name = name
        self.color = color
    @classmethod
    def description(cls,name,color):
        return cls(name, color)

    @staticmethod
    def isParrot(name):
        if name == "Parrot":
            return f"{name} can fly"


parrot = Bird.description('Parrot','Green')
print(parrot.name,"is",parrot.color)
print(Bird.isParrot("Parrot"))
