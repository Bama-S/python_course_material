#program to copy the contents of one file to another
with open('course.txt','rb') as file1:
    with open ('copied.txt','wb') as file2:
        text = file1.read()
        file2.write(text)
    print ("File is copied to file2")
