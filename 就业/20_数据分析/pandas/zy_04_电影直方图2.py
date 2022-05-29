import pandas as pd
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

print(df.head(1))
print(df.info())

# rating runtime 分布情况
# 选择图形，分布情况 -- 直方图

# 准备数据
runtime_data = df["Rating"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
print(max_runtime,min_runtime)
# num_bin =
num_bin_list = [1.6]

i = 1.6
while i <= max_runtime:
    i += 0.5
    num_bin_list.append(i)

# 设置图形的大小
plt.figure(figsize=(20,8),dpi=80)

plt.hist(runtime_data,num_bin_list)

# _x = [1.6]
# i = 1.6
# while i <= max_runtime + 0.5:
#     i = i + 0.5
#     _x.append(i)

plt.xticks(num_bin_list)
# print(len(_x))

plt.grid(alpha = 0.4)

plt.show()
