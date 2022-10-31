#To find the number of vowels

list1 = ["Chennai","Bangalore","University", "tamilnadu"]

for i in range(len(list1)):
    count = 0
    for j in list1[i]:
        if j == "a" or j == "e" or j =="i" or j == "o" or j == "u":
            count = count+1
    print ("the number of vowels", list1[i], "is ", count)
