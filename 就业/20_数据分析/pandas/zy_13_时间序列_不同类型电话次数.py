import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./911.csv"

df = pd.read_csv(file_path)

# print(df.head(1))
# print(df.info())

# 获取分类情况
# print(df["title"].str.split(": "))
temp_list = df["title"].str.split(": ").tolist()

# for i in temp_list 获取到[EMS, BACK PAINS/INJURY]   通过i[0]获取到EMS
cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

# 赋值
for cate in cate_list:
    # df["title"].str.contains(cate)  在title中包含cate的列
    # 布尔索引
    zeros_df[cate][df["title"].str.contains(cate)] = 1
    # break
# print(zeros_df)

# 取y轴索引    ----  很慢
# for i in range(df.shape[0]):
#     zeros_df.loc[i,temp_list[i][0]] = 1

sum_ret = zeros_df.sum(axis = 0)
print(sum_ret)
