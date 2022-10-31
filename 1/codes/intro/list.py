list1 = ["Chennai","Bangalore","Delhi","25","67",100,25.2,"University"]
strlist = [str(list1) for list1 in list1]
count=0
#print(strlist)
print("Elements that contain 'n' in the list:")
for i in range(0,len(strlist)):   
    n=strlist[i].find("n")
    if (n!= -1):
        print(strlist[i])
        count+=1
print("Number of elements containing 'n' in the list:", count)
