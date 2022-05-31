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

# set_index指定某一列作为索引
df.set_index("timeStamp",inplace=True)

# print(df.head(5))

# 统计出911数据中不同月份电话次数
# resample 降采样  --  按照月份进行读取数据  ----  统计每一个月份  ===   一月的全部读取 再读取二月 再读取三月....
count_by_month = df.resample("M").count()["title"]
print(count_by_month)

# 画图
_x = count_by_month.index
_y = count_by_month.values

# for i in _x:
#     print(dir(i))
#     break

# 对x轴进行格式化
_x = [i.strftime("%Y:%m") for i in _x]

plt.figure(figsize=(20,12),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x,rotation = 45)

plt.grid(alpha = 0.4)
plt.show()
