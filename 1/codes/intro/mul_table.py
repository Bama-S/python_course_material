n = int(input("enter the integer number to generate multiplication table "))
print("Multiplication table for", n)
print ("---------------------------")
for i in range(1,11):
    m = n*i
    print (n,"X",i,"=",m)
