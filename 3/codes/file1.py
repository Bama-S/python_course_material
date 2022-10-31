#file objects

f = open("course.txt",'a+')
print("Check whether the file is open or closed: ", f.closed)
print("Access mode of the file: ", f.mode)
print("Name of the file: ", f.name)
