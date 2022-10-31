#Change the column to a different datatype
import pandas as pd

ser1 = pd.Series(['10','20','30','40','50'])
print ("The series is \n ", ser1)
print("Now changing to numeric ")
ser2 = pd.to_numeric(ser1)
print(ser2)
