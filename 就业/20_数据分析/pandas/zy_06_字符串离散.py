import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

print(df["Genre"])

# 构造一个全为0的数组，列名为分类，如果某一条数据中分类出现，就让0变成1

# 统计分类列表   --  列表中列表 -- [[],[],[],[]]
temp_list = df["Genre"].str.split(",").tolist()

# i for j in temp_list for i in j 将列表中列表展开  用set去重 在转化为列表
genre_list = list(set([i for j in temp_list for i in j]))
print(temp_list)

# 构造全为0的数组   --  以为数组 series  二位  DataFrame

# 执行df.shape会返回一个元组，该元组的第一个元素代表行数，第二个元素代表列数
print(df.shape[0])

# columns 为列索引
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns= genre_list)

# 给每个电影出现分类的电影赋值为1
for i in range(df.shape[0]):
    # zero_df.loc[0,["Sci-fi","Mucisal"]] = 1
    # 取0行将 Sci-fi与Mucisal赋为1
    # loc a\按照标签取值
    zero_df.loc[i,temp_list[i]] = 1

# print(zero_df.head(3))

# 统计每个电影分类的数量和
# axis = 0 为竖轴
genre_count = zero_df.sum(axis = 0)
# print(genre_count)

# 排序
genre_count = genre_count.sort_values()

# 画图

"""
Series1 = pd.Series([1,2,3,4], index = ['a','b', 'c', 'd'])
Series1
#返回结果
Out[1]: 
a    1
b    2
c    3
d    4
dtype: int64

index 代表行索引
"""

_x = genre_count.index
_y = genre_count.values

# print("*" * 50)
# print(_x)
# print(_y)

plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x)

plt.grid(alpha = 0.4)

plt.show()

