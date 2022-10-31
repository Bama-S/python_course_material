class MyClass:
    def method(self):
        return 'instance method called'
    @classmethod
    def classmethod(cls):
        return 'class method called'

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())#object instance
print("-------------------")
print(obj.classmethod())#class instance
print("--------------------")
print(obj.staticmethod())#static method
print("------------------------")
print(MyClass.classmethod())
print("------------------------")
print(MyClass.staticmethod())
print("------------------------")
print(MyClass.method())
