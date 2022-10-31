# Series to find 1 -x + x^2-x^3-..

n = int(input("enter the value for n: "))
x = int(input("enter the value for x: "))
total = 0
for i in range(0,n+1):
    term = pow(x,i)
    neg = pow(-1,i) # alternate + and - ve terms
    full_term = term*neg
    total = total+full_term
print ("Series is ", total)
