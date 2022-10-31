#file input output error
try:
    #The access mode of the file is read, but the content is to be written.
    #So, exception of IOerror block gets executed
    with open("eg.txt",'r') as file:
        file.write("Adding a new statement. ")
except IOError:
    print ("Error working with file ")
else:
    print ("Written the statement to file")
