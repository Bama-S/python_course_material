#Example for keyboard interrupt error
try:
    inp = input()
    print ('Press Ctrl+C or any other key')
except KeyboardInterrupt:
    print ('Caused by KeyboardInterrupt')
else:
    print ('No exception occurred')
