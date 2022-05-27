import matplotlib.pyplot as plt
import numpy as np

# epoch,acc,loss,val_acc,val_loss
x_axis_data = [1, 2, 3, 4, 5, 6, 7]
y_axis_data1 = [68.72, 69.17, 69.26, 69.63, 69.35, 70.3, 66.8]
y_axis_data2 = [71, 73, 52, 66, 74, 82, 71]
y_axis_data3 = [82, 83, 82, 76, 84, 92, 81]

# 画图
plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='acc')  # '
plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='acc')
plt.plot(x_axis_data, y_axis_data3, 'go--', alpha=0.5, linewidth=1, label='acc')

## 设置数据标签位置及大小
for a, b in zip(x_axis_data, y_axis_data1):
    plt.text(a, b, str(b), ha='center', va='bottom', fontsize=8)  # ha='center', va='top'
for a, b1 in zip(x_axis_data, y_axis_data2):
    plt.text(a, b1, str(b1), ha='center', va='bottom', fontsize=8)
for a, b2 in zip(x_axis_data, y_axis_data3):
    plt.text(a, b2, str(b2), ha='center', va='bottom', fontsize=8)
plt.legend()  # 显示上面的label

plt.xlabel('time')
plt.ylabel('number')  # accuracy

# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
