#barplot with matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["June","July","August","September"])
y = np.array([100,150,79,85])
print("x values are", x)
print("y values are", y)
#Give the title
plt.title("Bar plot  - Month and exercise hours")
# Name x and y axis
plt.xlabel("x")
plt.ylabel("y")
plt.bar(x,y)
plt.show()
