#Multiplication of two arrays

import numpy as np

m1 = np.array([[13,45,67],[2,4,89],[45,67,89]])
m2 = np.ones((3,3))
m3 = np.dot(m1,m2)
print ("matrix 1 \n", m1)
print ("matrix 2 \n", m2)
print ("Matrix multiplication \n", m3)
