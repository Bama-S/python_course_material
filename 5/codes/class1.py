class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

A = Dog("Buddy", 9)
B = Dog("Miles",4)
print (A.name, A.age)
print (B.name, B.age)
print(A.species)
