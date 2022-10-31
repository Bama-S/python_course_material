#rsum of elements in a list

def total(listn):
    print ("Original list: ", listn)
    #find the total in the list using for loop
    total = 0
    for i in listn:
        total = total + i
    print ("Total using for loop =  ", total)

def totalbuiltin(listn):
    print ("Original list: ", listn)
    #find the total in the list
    total = sum(listn)
    print ("Total with builtin sum =  ", total)

nlist = [2,3,4,5,6,100]
total(nlist)
totalbuiltin(nlist)
