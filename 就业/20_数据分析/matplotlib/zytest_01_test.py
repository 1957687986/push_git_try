from matplotlib import pyplot as plt

# 设置图片 / figsize 图片大小 dpi 每英寸上点的个数 - 是图像更清晰
# 通过实例化一个figure并传入参数，能够在后台自动使用figure实例
# fig = plt.figure(figsize=(20,20),dpi=20)

# 数据在x轴的位置，是一个可迭代对象
x = range(2,26,2)

# 数据在y轴的位置，是一个可迭代对象
y = [15,13,14,5,17,20,25,26,26,27,22,18]

# x轴与y轴的数据组成了所有要绘制出的坐标
# 分别是(2,15)、(4,13)、......

# 传入x和y，通过plot绘制折线图
plt.plot(x,y)

# 列表解析式
# x_tabel = [i/2 for i in range(4,49)]
# 绘制x轴刻度
# plt.xticks(x)
# plt.xticks(range(2,25))
# plt.xticks(x_tabel)
plt.yticks(range(min(y),max(y)+1))

# 保存
# plt.savefig("./figTest01.png")
# plt.savefig("./figTest01.svg")

# 在程序运行时展示图片
plt.show()