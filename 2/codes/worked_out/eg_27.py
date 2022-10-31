#smallest number in the list

def smallloop(listn):
    print ("Original list: ", listn)
    #find the smallest number in the list using for loop
    minimum = listn[0]
    for i in listn:
        if minimum > i:
            minimum = i
    print ("Minimum using for loop =  ", minimum)

def smallbuiltin(listn):
    print ("Original list: ", listn)
    #find the smallest number using builtin function
    minimum = min(listn)
    print ("Minimum with builtin function =  ", minimum)

def smallsort(listn):
    print ("Original list: ", listn)
    #find the smallest number using sort function
    listn.sort()
    print ("Sorted list ",listn )
    print ("Minimum with sort function =  ", listn[0])

def dashedline():
    print ("----------------------------------------------")


nlist = [2,3,4,5,6,100]
smallloop(nlist)
dashedline()
smallbuiltin(nlist)
dashedline()
smallsort(nlist)
dashedline()
