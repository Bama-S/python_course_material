#count number of tabs, spaces and newline characters in a text
with open ('poem.txt','r') as file:
    text = file.read()
    count_tab = 0
    count_space = 0
    count_newline = 0
    for char in text:
        if char == '\t':
            count_tab += 1
        if char == ' ':
            count_space +=1
        if char =='\n':
            count_newline += 1
print ("Tabspace = ", count_tab)
print ("Spaces = ", count_space)
print ("newlines = ", count_newline) 
