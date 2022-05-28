import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")
plt.rcParams['axes.unicode_minus'] =False

# 加载国家数组
us_data_path = "./USvideos.csv"
uk_data_path = ""

t_us = np.loadtxt(us_data_path,delimiter=",",dtype=int)
t_uk = np.loadtxt(uk_data_path,delimiter=",",dtype=int)

t_us_comment = t_us[:, 10]
t_uk_like = t_us[:,8]

plt.figure(figsize=(20,8),dpi=80)

plt.scatter(t_uk_like, t_us_comment)

plt.show()