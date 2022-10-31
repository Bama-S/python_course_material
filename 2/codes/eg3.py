#sort in ascending order

n = int(input("enter the number of elements in the list: "))
numlist = []
for i in range(n):
    num = int(input("enter number " ))
    numlist.append(num)
print ("Entered numbers are: ")
print (numlist)
ascendlist = sorted(numlist)
print ("Sorted numbers are ")
print(ascendlist)
