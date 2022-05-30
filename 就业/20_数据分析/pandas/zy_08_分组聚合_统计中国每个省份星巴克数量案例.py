import pandas as pd
import numpy as np

file_path = "./directory.csv"

df = pd.read_csv(file_path)

# china_data = df[df["Country"] == "CN"]
# print(china_data)

# grouped为DataFrameGroupBy对象，可迭代
# grouped中的每一个元素都是一个元组
# 元组里面是（索引（分组的值）），分组之后的DataFrame
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
# print(grouped)


# 数据按照多个条件进行分组  ---  返回series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)

# 数据按照多个条件进行分组  ---  返回DataFrame  -- 下面三种都可以
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped2 = df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]

print(grouped1,type(grouped1))
print("-" * 100)
print(grouped2,type(grouped2))
print("-" * 100)
print(grouped3,type(grouped3))
