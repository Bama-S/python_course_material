def add (x,y):
    total = x+y
    print (x,"+",y,"is", total)

def sub (x,y):
    total = x-y
    print (x,"-",y,"is", total)

def mul (x,y):
    total = x*y
    print (x,"*",y,"is", total)

def div (x,y):
    total = x/y
    print (x,"/",y,"is", total)

n = int(input("Enter the first number:"))
m = int(input("Enter the second number:"))
add (n,m)
sub (n,m)
mul (n,m)
div (n,m)
