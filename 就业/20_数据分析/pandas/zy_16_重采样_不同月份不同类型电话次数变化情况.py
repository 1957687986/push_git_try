import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./911.csv"

df = pd.read_csv(file_path)

# print(df.head(5))
# print(df.info())
# print("-" * 50)

# 把时间字符串转化为时间类型，设置为索引
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

# 设置添加列，表示分类
# print(df["title"].str.split(": "))
temp_list = df["title"].str.split(": ").tolist()
# for i in temp_list 获取到[EMS, BACK PAINS/INJURY]   通过i[0]获取到EMS
cate_list = [i[0] for i in temp_list]
# print(cate_list)
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
# 在df中添加cate的一列
# 取df中的第一个数据名再从data_df中找到数据进行添加  ===   通过索引进行添加
# 将一个DataFrame赋值到另一个DataFrame中时，一定要注意索引要保持一致，否则会出现NaN情况
df["cate"] = cate_df

# set_index指定某一列作为索引
df.set_index("timeStamp",inplace=True)

plt.figure(figsize=(20, 12), dpi=80)

# 分组  ==
# groupby 之后是一个可迭代的对象
# 为一个元组，里面有两个数据，用group_name,group_data进行接收
for group_name,group_data in df.groupby(by="cate"):
    # 对不同的分类都进行绘图
    # print(group_name)
    # print("-" * 50)
    # print(group_data)
    # break
    count_by_month = group_data.resample("M").count()["title"]

    # 画图
    _x = count_by_month.index
    _y = count_by_month.values

    # 对x轴进行格式化
    _x = [i.strftime("%Y:%m") for i in _x]

    plt.plot(range(len(_x)), _y,label = group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc = "best")
plt.grid(alpha=0.4)
plt.show()
