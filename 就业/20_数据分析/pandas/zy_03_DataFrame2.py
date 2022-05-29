from pymongo import MongoClient
import pandas as pd

client = MongoClient()
collcetion = client["douban"]["tv1"]
data = list(collcetion.find())
data1 = collcetion.find()

data_list = []

for i in data1:
    temp = {}
    temp["info"] = i["info"]
    temp["rating_count"] = i["rating"]["count"]
    temp["rating_value"] = i["rating"]["value"]
    temp["title"] = i["title"]
    temp["country"] = i["tv_category"]
    temp["directors"] = i["directors"]
    data_list.append(temp)

# t1 = data[0]
# t1 = pd.Series(t1)
# print(t1)

df = pd.DataFrame(data_list)
# print(df)

# 显示前几行 -- 默认前五行
print(df.head())

# 显示后几行 -- 默认五行
print(df.tail())

# 展示df的概览
print(df.info())
# 统计当前数字列的最大、最小、平均。。。
print(df.describe())
