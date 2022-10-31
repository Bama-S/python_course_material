import pandas as pd

data = {"fruits": ["apple", "apricot","grapes", "lemon"], "calories":[95,17,62,17]}
df = pd.DataFrame(data)
df.to_csv("fruits.csv")
print(df)
print("The first row")
print(df.loc[0])
