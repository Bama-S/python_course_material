#multiplication table
#using for loop
x = int(input("Multiplication table of "))
n = int(input("till "))
for i in range(1, n+1):
   print(x,"*",i,"=",x*i)

#using while loop
n=int(input("Enter a number: "));
i=0;
while i<n:
   i+=1;
   print(n,'*',i,'=',n*i)
