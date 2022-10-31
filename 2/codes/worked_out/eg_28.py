#print the even numbers in the list

def even(listn):
    print ("Original list: ", listn)
    for i in range(0,len(listn),2):
        print ("Index =  ", i, " number = ", listn[i])

nlist = [2,3,4,5,6,100]
even(nlist)
