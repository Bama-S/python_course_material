#sum of series 1+x+x^2+...

x = int(input("enter the value for x: "))
n = int(input("enter the value for n: "))
total = 0
for i in range(0,n+1):
    term = pow(x,i)
    #print (term)
    total = total+term
print ("The sum is", total)
