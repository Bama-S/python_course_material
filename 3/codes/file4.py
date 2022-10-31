#file objects
# opening file
f = open("course.txt",'r+')
str = f.read(10)
print ("Reading 10 characters from file....")
print(str)
print ("--------------")

# check the current position
position1 = f.tell()
print ("The current file position: ", position1)
print ("--------------")
#reposition pointer to a particular offset
position2 = f.seek(position1,0)
str = f.read(30)
print ("Reading again.....")
print (str)

#close the file
f.close()
