#program to print a random line from the file

import random
with open ('poem.txt','r') as file:
    lines = file.readlines()
    print (random.choice(lines))
