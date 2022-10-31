#This is an example of list in python

list1 = ["Chennai","Bangalore","Delhi","25","67",100, 25.2,"University"]
# this program is to indicate the slicing aspect
slice1 = list1[1:3]
slice2 = list1[1:]
slice3 = list1[:8]
slice4 = list1[:]
slice5 = list1[-5:-1]
slice6 = list1[:-3]
#print(slice6)
for i in range(0,len(list1)):
    print (i,list1[i])

if 100 in list1:
    print("100 is present in the list")


# See where "n" is appearing and if appearing, count the number of elements available in this list
