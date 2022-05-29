import pandas as pd
import numpy as np

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# print(df.info())

print(df.head(1))


# 获取电影平均评分
print(df["Rating"].mean())

# 获取导演人数
# set函数是对列表作集合操作，可以去重
# print(len(set(df["Director"].tolist())))

# df["Director"].unique() 直接获取一个列表，不可重复
print(len(df["Director"].unique()))


# 获取演员人数

temp_actores_list = df["Actors"].str.split(",").tolist()
# temp_actores_list 为一个列表，列表中数据也为列表
# 下面两个for为从列表中取到一个数据（列表）,再从这个列表中读取数据
print(temp_actores_list)
actores_list = [i for j in temp_actores_list for i in j]
# flatten -- 变成一维
# actores_list = np.array(temp_actores_list).flatten().tolist()

actores_num = len(set(actores_list))

print(actores_num)