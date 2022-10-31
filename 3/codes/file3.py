#file objects

f = open("course.txt",'a+')
str = "Python supports text files extensively. "
f.write(str)
print ("The content is written to the file")
f.close()
