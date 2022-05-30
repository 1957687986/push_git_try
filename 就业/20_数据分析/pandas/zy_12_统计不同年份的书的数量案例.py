import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./books.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 删除这一列有缺失的数据
# pd.notnull 是一个bool类型的结果 ，df再取bool索引来取不为nan的值
# df.dropna()也为删除

# 不同年份书的数量
# data1 = df[pd.notnull(df["original_publication_year"])]
#
# grouped = data1.groupby(by="original_publication_year").count()["title"]

# 不同年份书的平均评分情况
# 去除original_publication_year中的nan的行
data1 = df[pd.notnull(df["original_publication_year"])]

grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()

print(grouped)

_x = grouped.index
_y = grouped.values

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

# astype 为去除小数
plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation = 45)

plt.show()
