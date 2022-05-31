import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./911.csv"

df = pd.read_csv(file_path)

# print(df.head(5))
# print(df.info())

# 获取分类情况
# print(df["title"].str.split(": "))
temp_list = df["title"].str.split(": ").tolist()

# for i in temp_list 获取到[EMS, BACK PAINS/INJURY]   通过i[0]获取到EMS
cate_list = [i[0] for i in temp_list]
# print(cate_list)
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

df["cate"] = cate_df

# print(df.head(5))
# 此方式为添加一行，最后统计数据
# print(df.groupby(by="cate").count()["title"])

# 处理时间序列
"""
'2020-05-31', '2020-06-10', '2020-06-20', '2020-06-30',
               '2020-07-10', '2020-07-20', '2020-07-30', '2020-08-09',
               '2020-08-19', '2020-08-29', '2020-09-08', '2020-09-18',
               '2020-09-28', '2020-10-08',
"""
data_time1 = pd.date_range(start="20200531",end="20221001",freq="10D")
print(data_time1)

"""
['2020-05-31', '2020-06-01', '2020-06-02', '2020-06-03',
               '2020-06-04', '2020-06-05', '2020-06-06', '2020-06-07',
               '2020-06-08', '2020-06-09'],
"""
data_time2 = pd.date_range(start="20200531",periods=10,freq="D")
print(data_time2)
