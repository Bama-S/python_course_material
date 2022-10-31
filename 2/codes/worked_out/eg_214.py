#Simulate a word jumble game for 10 attempts
word = "reuosc"
print ("The word in jumbled form is ", word)
print ("The game starts ")
print ("------------------")
print ("You have ten chances to type the correct word")
n = 10
attempt = 1
while n>0:
    w = str(input("enter the word "))
    wrd = w.lower()
    if w == "course":
        print ("You are correct")
        print ("Number of attempts ", attempt)
        break
    else:
        print ("Try again")
        attempt +=1
    n = n-1
    if n ==0:
        print("You have lost the game")
