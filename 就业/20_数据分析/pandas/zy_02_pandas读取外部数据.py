import pandas as pd
from pymongo import MongoClient

# pandas读取csv中的文件
df = pd.read_csv("./USvideos.csv")
print(df)

client = MongoClient()
collection = client["douban"]["tv1"]

data = list(collection.find())

t1 = data[0]

t1 = pd.Series(t1)

print(t1)
