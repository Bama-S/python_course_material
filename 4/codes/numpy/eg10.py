#column wise sum and row wise sum
import numpy as np

m1 = np.array([[13,45,67],[2,4,89],[45,67,89]])
columnsum = np.sum(m1,axis=0)
print("Column wise sum", columnsum)
rowsum = np.sum(m1,axis = 1)
print("Row wise sum", rowsum)
