#permutate the given string
from itertools import permutations
word = str(input("Enter the word: "))
word = word.lower()
perm_list = []
for i in permutations(word):
    perm_list = perm_list+ ["". join(i)]

perm_num = len(perm_list)
print ("Total number of jumbled words are ", perm_num)
print ("The jumbled words are ")
print (perm_list)
