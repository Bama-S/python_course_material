#illustration of overflow exception
import math
try:
    n = math.exp(863)
except OverflowError:
    print("Overflow exception is raised. ")
else:
    print ("Success, the value of e^(5) is ", n)
