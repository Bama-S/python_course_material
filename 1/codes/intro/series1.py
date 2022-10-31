#factorial of a number

n = int(input("enter the number to find the factorial"))
fact = 1
for i in range(n,1,-1):
    fact = fact*i
print("Factorial of number",n, "is", fact)
