try:
    #n = 5
    print(n)
except NameError:
    print("Variable not defined")
except:
    print("Something else is wrong")
else:
    print("Nothing is wrong")
finally:
    print("relevant blocks are executed")
