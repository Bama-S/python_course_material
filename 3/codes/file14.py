#program to copy the contents of one file to another
with open('course1.txt','r') as file1:
    with open ('copied.txt','a+') as file2:
        text = file1.readlines()
        for line in text:
            words = line.split()
            words.reverse()
            reverse_sent = " ".join(words)
            print (reverse_sent)
            file2.write(reverse_sent)
            file2.write('\n')
        #file2.write(text)
    #print ("File is copied to file2")
