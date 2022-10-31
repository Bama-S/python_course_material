#Example of 2-D and 3-D array
import numpy as np
#creation of 2-d array
arr = np.array([[1,2,3],[4,6,8]])
print("The array is", arr)
#shape
print("The shape of array is", arr.shape)
print("The dimension of array is", arr.ndim)

#creation  of 3-d array
arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print ("The array is", arr2)
print ("The shape of an array is ", arr2.shape)
print ("The dimension of array is", arr2.ndim)
