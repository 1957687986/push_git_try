import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")
plt.rcParams['axes.unicode_minus'] =False

# 加载国家数组
us_data_path = ""
uk_data_path = ""

t_us = np.loadtxt(us_data_path,delimiter=",",dtype=int)
t_uk = np.loadtxt(uk_data_path,delimiter=",",dtype=int)

# 取评论数
t_us_comments = t_us[:,-1]

# 选择比5000小的数据
t_us_comments =  t_us_comments[t_us_comments <= 5000]

print(t_us_comments.max(),t_us_comments.min())

d = 250
bin_nums = (t_us_comments.max()-t_us_comments.min()) // d

# 绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,bin_nums)

plt.show()