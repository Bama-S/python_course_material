#sum of series 1+x/1!+x^2/2!+...

x = 2
n = 3
total = 0

for i in range(0,n+1):
    term = pow(x,i)
    fact = 1
    
    #print (term)
    total = total+term
print (total)
