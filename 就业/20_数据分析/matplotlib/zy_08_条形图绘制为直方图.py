from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

matplotlib.rc("font",family = "KaiTi")
plt.rcParams['axes.unicode_minus'] =False

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
# 统计之后的数据
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.bar(range(len(quantity)),quantity,width = 1)

# x轴刻度
_x = [i - 0.5 for i in range(13)]
_xtick_labels = interval + [150]

plt.xticks(_x,_xtick_labels)

# print(len(interval),len(width),len(quantity))

# 网格
plt.grid()

plt.show()