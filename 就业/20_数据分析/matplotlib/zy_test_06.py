import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(0, 5)  # X轴的坐标范围
Y = np.arange(0, 9)  # Y轴的坐标范围

Z_list = []
for i in range(0, 9):
    Z_list.append(np.ones(5) * i)
Z = np.array(Z_list)
print(Z.shape) # (9, 5)

xx, yy = np.meshgrid(X, Y)  # 网格化坐标
X, Y = xx.ravel(), yy.ravel()  # 矩阵扁平化 拉成一维向量
bottom = np.zeros_like(X)  # 设置柱状图的底端位值
Z = Z.ravel()  # 扁平化矩阵

width = height = 1  # 每一个柱子的长和宽

# 绘图设置
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
clr = plt.cm.jet(Z.ravel()/float(Z.max()))
ax.bar3d(X, Y, bottom, width, height, Z, shade=True, color=clr)

# 坐标轴设置
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z(value)')

# 保存和显示
# plt.savefig('./plot_3d.png', dpi=400)
plt.show()
