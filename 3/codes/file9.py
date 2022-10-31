#create 10 text files in a new directory and enter the string
# "This is file 1, This is file 2,.. " in each of the files
import os
directory = "tenfiles"
os.mkdir(directory)
for i in range(11):
    fname = "tenfiles/file"+str(i)
    with open(fname,'w+') as f:
        content = "This is file " + str(i)
        f.write(content)
