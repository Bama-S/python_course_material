#deliberately to raise an exception
try:
    n = 5
    print(n)
    raise ValueError # deiberately raising an exception
except:
    print("Exception raised")
