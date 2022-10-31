#join two tuple and print unique elements

tuple1 = (2,3,4,5)
tuple2 = (5,6,7,8)

print ("Tuple1 is ", tuple1)
print ("Tuple2 is ", tuple2)

if tuple1[-1] == tuple2[0]:
    tuple3 = tuple1+ tuple2
    unique = set(tuple3)
    print ("The unique elements are: ", unique)
else:
    print ("The last element of one tuple is not equal to the first element of second tuple")
