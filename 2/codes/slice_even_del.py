#program to enter even numbers to a list and delete

even = []#initialize the list
for i in range(0,20):
    if i % 2 == 0:
        even = even+[i] #convert i to list and concatenate with even at every step
print ("Even numbers between 0 and 20 are: ")
print (even)
print ("Deleting the list now")
del even[:]
print ("The list is empty")
print (even)
