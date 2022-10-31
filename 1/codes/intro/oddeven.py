#odd/even numbers from 1 to 100

print("Enter a range")
x=int(input("From: "))
n=int(input("To: "))

print("Even numbers from",x,"to",n)
for i in range(x,n+1):
    if(i%2==0):
        print(i)
        
print("Odd numbers from",x,"to",n)
for i in range(x,n+1):
    if(i%2!=0):
        print(i)

