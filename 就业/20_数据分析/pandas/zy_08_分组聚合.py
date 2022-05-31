import pandas as pd
import numpy as np

file_path = "./directory.csv"

df = pd.read_csv(file_path)

# print(df.head(1))
# print(df.info())

# 在pandas中分组操作比较简单    --- df.groupby(by="columns_name")
grouped = df.groupby(by="columns_name")

print(grouped)

# DataFrameGroupBy
# 可以进行遍历

"""
for i,j in [[1,2],[2,3]]:
    print(i,j)
"""

# for i,j in grouped:
#     print(i)
#     print("-" * 100)
#     print(j)
#     print("*" * 100)
# 直接找到US数据
# df[df["Country"] = "US"]

# 调用聚合方法
country_count = grouped["Brand"].count()
print(country_count["US"])
print(country_count["CN"])