#check whether the tuple of immediate even number indices are same

tuple1 = (1,0,1,2,1,3,1)
for i in range(0,len(tuple1)-2):
    if tuple1[i] == tuple1[i+2]:
        print ("indices ", i, i+1, "are same with ")
        print (tuple1[i], " ", tuple1[i+2])
