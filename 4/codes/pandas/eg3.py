#create a random sequence of 6X4 array with numpy
# Create a dataframe and add labels as A,B,C,D
import numpy as np
import pandas as pd

m = np.random.random((6,4))
df = pd.DataFrame(m,columns = list('ABCD'))
print (df)
