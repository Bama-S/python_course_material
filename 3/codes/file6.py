#program to display the count of words in each sentence
with open('course.txt','r') as file:
    for line in file:
        print ("Actual Sentence: ", line)
        words = line.split()
        print("Number of words = ", len(words))
