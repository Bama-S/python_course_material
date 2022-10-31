#With same dataframe as above, get columns A,C first three rows
import numpy as np
import pandas as pd

m = np.random.random((6,4))
df = pd.DataFrame(m,columns = list('ABCD'))
splitdf = df[['A','C']]
print(splitdf[0:3])
