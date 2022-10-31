#scatterplot with matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = [2,3,5,8,3,4,10,9,7,8]
y = [1,2,1,3,4,5,6,7,3,5]
print("x values are", x)
print("y values are", y)
#Give the title
plt.title("Scatter plot")
# Name x and y axis
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(x,y)
plt.show()
