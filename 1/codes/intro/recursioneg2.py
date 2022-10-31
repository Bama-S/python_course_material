def sn(numList):
    global n
    n = n+1
    print ("The number of times the function executes ", n)
    if len(numList) == 1:
        return numList[0]
    else:
        r =  numList[0]
        print ("The function takes the value of r as", r)
        s = sn(numList[1:])# recursion step
        print ("The value of s in this step is", s)
        return r + s
n = 0
print (sn([6,8,10,5,7]))
