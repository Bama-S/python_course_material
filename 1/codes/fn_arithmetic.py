def addition(n1,n2):
    global total
    total = n1+n2
    return total

def subtraction(n1,n2):
    global sub
    sub = n1-n2
    return sub

x = 78
y = 10
print ("Addition of two numbers ")
a = addition(x,y)
print (total)
print ("Subtraction of two numbers")
b = subtraction(x,y)
print (sub)
