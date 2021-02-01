import pandas as pd

data = pd.read_excel("ss.xlsx")
print(data)
print(data.mean())
print(data.min())
print(data.max())
print(data.var())
print(data.std())
print(data.sort_values(by=(['语文']+['数学']+['英语']),ascending=False))