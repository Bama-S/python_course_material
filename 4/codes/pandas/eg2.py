import pandas as pd

data = pd.read_csv('fruits.csv')
df = pd.DataFrame(data)
print(df)
print ("----------------------")
print("Sum: ",df["calories"].sum())
print("Mean: ",df["calories"].mean())
print("Maximum: ",df["calories"].max())
print("Minimum: ",df["calories"].min())
