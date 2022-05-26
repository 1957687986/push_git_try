from matplotlib import pyplot as plt
from random import *
import matplotlib

# matplotlib默认不支持中文
# matplotlib.rc("font", family = 'MicroSoft YaHei',weight = "blod")

matplotlib.rc("font",family='KaiTi')

x = range(0,120)

y = [randint(20,35) for i in range(120)]

plt.plot(x,y)

# 调整x轴刻度
_x = list(x)
_xtick_label = ["10点{}分".format(i) for i in range(60)]
_xtick_label += ["11点{}分".format(i) for i in range(60)]
# 取步长。数字与字符串长度一样 rotation 为旋转度数
plt.xticks(_x[::10],_xtick_label[::10],rotation = 45)

# 添加描述信息
# plt.xlabel("时间")
# plt.ylabel("温度/℃")
# plt.title("10点到12点每分钟气温的变化情况")

plt.show()