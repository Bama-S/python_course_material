#Sum of first n numbers
total = 0
n = int(input("enter the number "))
for i in range(n+1):
    total = total+i
print ("Total of first ",n, "numbers is ", total)
