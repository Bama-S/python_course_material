#5X5 array with random values and find mean, min and max
import numpy as np
m = np.random.random((5,5))
minimum = m.min()
maximum = m.max()
mean = m.mean()
print("The array is ", m)
print("The minimum number is ", minimum)
print("The maximum number is ", maximum)
print("The mean is ", mean)
