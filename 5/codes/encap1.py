# Encapsulation example
class Banana:
    def __init__(self):
        self.__length = "6 cms"#private variable

    def long(self):
        print("The maximum length: {}".format(self.__length))
    #create a function with length as argument
    def setlength(self,length):
        #assign the value of length to the variable
        self.__length=length

b = Banana()
b.long()
b.__length = "12 cms"
print("The length is changed to 12 cms in the program, but...")
b.long()
print("Pass the value of length as 12 cms to function.")
b.setlength("12 cms")
print("The value should change now.")
b.long()
