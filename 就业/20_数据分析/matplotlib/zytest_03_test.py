from matplotlib import pyplot as plt

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

x = [i for i in range(13,33)]

plt.plot(x,y)

plt.xticks(x[::2])

plt.xlabel("age")
plt.ylabel("num")

# 绘制网格 alpha 设置网格透明度
plt.grid(alpha = 0.4)

plt.show()