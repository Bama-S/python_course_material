import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10) # values in x axis
y = 2*x # double x
z = x*x # x squared
print("x values are", x)
print("y values are", y)
print("z values are", z)
#Give the title
plt.title("An example plot")
# Name x and y axis
plt.xlabel("x")
plt.ylabel("y")
#plot x with y and x with z
plt.plot(x,y)
plt.plot(x,z)
# add legend to lower right corner
plt.legend(["2x", "x-squared"], loc ="lower right")
plt.grid()
plt.show()
