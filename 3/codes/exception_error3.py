try:
    print(n)
except NameError:
    print("Variable not defined")
except:
    print("Something else is wrong")
