#demonstration of value error
def gettype(num):
    print("The actual type is of ", num, "is", type(num))
    print ("Now, try convert this type to int")
    try:
        int(num)
    except ValueError:
        print("Throwing exception......")
        print("String cannot be converted  to integer value")

n = '15.64'
gettype(n)
