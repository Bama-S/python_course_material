def listsum(numList):
   global n
   n += 1
   #print "the function is called with list", numList
   if len(numList) == 1:
        #print "number of times the function is called", n
        return numList[0]
   else:
        #print "numlist", numList
        r =  numList[0]
        #print "intermediate value of 1st element", r
        s = listsum(numList[1:])
        #print "intermediate value during the addition of elements", s
        return r + s
n = 0
print (listsum([2,4,6,8,3,9]))
