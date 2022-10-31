#get integers from user and save it in the list. Find the cube.

numlist = []
n = 1
while n>0:
    num = int(input("Enter the positive number to be added to the list, to stop enter -1:  "))
    if num > 0:
        numlist = numlist+[num]
        n = n+1
    else:
        n = -1

print ("The entered numbers are ", numlist)

cube = []
for i in numlist:
    cube = cube +[i**3]
print ("The cube of entered numbers ", cube)
