#Add and subtract two arrays
import numpy as np
m1 = np.array([[13,45,67],[2,4,89],[45,67,89]])
m2 = np.ones((3,3))
print ("matrix 1 \n", m1)
print ("matrix 2 \n", m2)
m3 = m1+m2
print("Addition of two matrices \n", m3)
m4 = m1 - m2
print("Subtraction of two matrices \n", m4)
