#demonstration of keyboard interrupt error

n = int(input("Enter a number: "))
try:
    square = n*n
except KeyboardInterrupt:
    #print ('You have pressed Ctrl+C')
    print ("Keyboard interrupt error")
else:
    print ("No keyboard interrupt error")
