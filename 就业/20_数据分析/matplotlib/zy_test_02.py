from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib
import random

matplotlib.rc("font",family = "KaiTi")
plt.rcParams['axes.unicode_minus'] =False

# 1.准备数据x,y
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(5, 9) for i in x]

# 2.创建画布
# plt.figure(figsize=(20,8),dpi=200)
figure,axes = plt.subplots(nrows=1,ncols=2,figsize=(20,8),dpi=200)

# 3.绘制图像
axes[0].plot(x,y_shanghai,color="r",linestyle="--",label="上海")
axes[1].plot(x,y_beijing,color="b",label="北京")

# 显示图例
axes[0].legend()
axes[1].legend()

# 修改x,y刻度
# 准备x的刻度说明
x_label = ["11点{}分".format(i) for i in x]
axes[0].set_xticks(x[::10])
axes[0].set_xticklabels(x_label[::10])
axes[0].set_yticks(range(0,40,5))

axes[1].set_xticks(x[::10])
axes[1].set_xticklabels(x_label[::10])
axes[1].set_yticks(range(0,40,5))

# 添加网格
axes[0].grid(linestyle="--",alpha=0.5)
axes[1].grid(linestyle="--",alpha=0.5)

# 添加描述信息
axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度")
axes[0].set_title("北京11点到12点1小时内每分钟的温度变化折线图")
axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度")
axes[1].set_title("上海11点到12点1小时内每分钟的温度变化折线图")

# 4.显示图像
plt.show()
