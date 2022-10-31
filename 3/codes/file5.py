#program to display the contents of file in list.

f = open('course.txt','r')
print (list(f))
f.close()
