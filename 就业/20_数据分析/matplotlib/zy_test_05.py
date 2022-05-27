import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif']=['SimHei'] # 图表中的中文字，选择 SimHei 字体
mpl.rcParams['axes.unicode_minus']=False # 一般使用ASCII hython模式处理坐标轴负刻度值的情况

# some simple data
x = [1,2,3,4,5]
y = [6,10,4,5,1]
y1 = [2,6,3,8,5]

# create bar
plt.bar(x,y,
        align='center',
        color='#66c2a5',
        tick_label=['A','B','C','D','E'],
        label='班级A')

plt.bar(x,y1,
        align='center',
        bottom=y,
        color='#8da0cb',
        label='班级B')

# set x,y_axis label
plt.xlabel('测试难度')
plt.ylabel('试卷份数')

plt.legend()
plt.show()
