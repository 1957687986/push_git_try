import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./PM2.5archive/BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

# print(df.head(5))
# print(df.info())

# 把分开的时间字符串通过PeriodIndex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year = df["year"],month = df["month"],day = df["day"],hour = df["hour"],freq="H")
# print(period)

df["datetime"] = period
# print(df.head(10))

# 把datetime 设置为索引  inplace 为原地修改
df.set_index("datetime",inplace=True)

# 降采样
df = df.resample("7D").mean()

# 处理缺失数据  ---   删除缺失数据
# print(df["PM_US Post"])
# 去除NaN
data = df["PM_US Post"].dropna()
# 中国的数据有太多nan，去nan之后会在画图时数据前移
data_china = df["PM_Dongsi"]

# 画图
_x = data.index
_x = [i.strftime("%Y.%m.%d") for i in _x]
_x_china = [i.strftime("%Y.%m.%d") for i in data_china.index]
_y = data.values
_y_china = data_china.values

# print(_y)
# print("-" * 50 )
# print(_y_china)

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y,label = "US_POST")
plt.plot(range(len(_x_china)),_y_china,label = "CN_POST")

plt.xticks(range(0,len(_x),10),list(_x)[::10],rotation = 45)

plt.legend(loc = "best")

plt.grid(alpha = 0.4)

plt.show()
