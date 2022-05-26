from matplotlib import pyplot as plt
import matplotlib

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,2,1,1,3,4,5,2,1,0,4,1,1,2,3,1,4,2,2,1]

matplotlib.rc("font",family = "KaiTi")

x = [i for i in range(13,33)]

plt.plot(x,y_1,label = "自己",color = "orange",linestyle = ":")
plt.plot(x,y_2,label = "同桌",color = "cyan",linestyle = "--")

plt.xticks(x[::2])

plt.xlabel("age")
plt.ylabel("num")

# 绘制网格 alpha 设置网格透明度
plt.grid(alpha = 0.4,linestyle = "--")

# 添加图例  plt.plot(x,y_1,label = "自己")
# 图例与label对应  loc代表图例位置
plt.legend(loc = 2)

plt.show()