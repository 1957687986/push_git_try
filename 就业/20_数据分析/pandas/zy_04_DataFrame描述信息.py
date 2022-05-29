from pymongo import MongoClient
import pandas as pd
import numpy as np

df = pd.read_csv("./USvideos.csv")
print(df.head())
print(df.info())

# dataframe中排序方法  ascending 为升序
df = df.sort_values(by="views",ascending=False)
# print(df.tail(10))

# pandas取行或列注意点
# 1. 方括号写数组，表示取行，对行进行操作
# 2. 写字符创，表示取列，对列进行操作
print(df[:10])
print(df[:10]["tags"])

t3 = pd.DataFrame(np.arange((12)).reshape(3,4),index=list("abc"),columns=list("wxyz"))

# 取a行z列 -- 通过标签获取
print(t3.loc["a","z"])
# print(type(t3.loc("a","z")))

# 通过位置获取  -- 第几行第几列
print(t3.iloc[1,:])
print(t3.iloc[[0,2],[2,1]])