import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./directory.csv"

df = pd.read_csv(file_path)
df = df[df["Country"] == "CN"]
# print(df)

data1 = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:20]

# print(data1)
# print(type(data1))
# pandas.Series( data, index, dtype, name, copy)
# index：数据索引标签，如果不指定，默认从 0 开始
_x = data1.index
_y = data1.values
# print(_y)

# 画图
plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x)

plt.grid(alpha = 0.4)
plt.show()
