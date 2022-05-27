# 简单了解
import numpy as np

# youtube视频数据集
us_file_path = "C:/Users/19576/Desktop/uc.csv"
uk_file_path = ""

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int")
#
# print(t1)
#
#
# t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
#
# print("*" * 100)
#
# print(t2)

t1 = np.loadtxt(us_file_path)

# 取行
print(t1[8])

# 取多行
print(t1[2:])

# 取不同的行
print(t1[[2,8,10]])

# 取行
print(t1[1,:])
print(t1[2:,:])
print(t1[[2,10,15],:])

# 取列
print(t1[:,1])

# 取多行多列
a = t1[2,3]
print(a)
print(type(a))

# 取交叉点位置
b = t1[2:5,1:4]
print(b)

# 取多个不相邻的点[0,2],[2,1],[2,3]
c = t1[[0,2,2],[2,1,3]]
print(c)
