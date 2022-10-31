#program to reverse the number
n = int(input("enter an integer "))
reverse = 0
while n>0:
    rem = n%10
    n = n//10
    reverse = (reverse*10) + rem
print ("The reversed number is ", reverse)
