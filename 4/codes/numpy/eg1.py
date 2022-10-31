#creation of vector with first 6 values and print the dimension.
#Convert it to matrix of 2X3
import numpy as np

m1 = np.arange(1,7)
print("The vector is", m1)
print("The shape is ", m1.shape)
m2 = m1.reshape(2,3)
print("Converted to 2X6: ",  m2)
print("The shape of m2 is ", m2.shape)
