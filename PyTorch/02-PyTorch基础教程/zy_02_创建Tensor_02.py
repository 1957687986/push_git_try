import numpy as np
import torch

"""
随机初始化
"""
print("随机初始化.................")

# rand随机初始化0~1之间的数值，不包括1
print(torch.rand(3,3))

a = torch.rand(3,3)

# 读出a.shape送入rand函数
print(torch.rand_like(a))

# randint()需要指定最大值最小值 1  10，形状
print(torch.randint(1,10,[3,3]))

# 正态分布
print(torch.randn(3,3))

print(torch.normal(mean=torch.full([10],0),std=torch.arange(1,0,-0.1)))

# full函数为生成长度为10全为0的向量
# 方差std从1到0不停的减小
b = torch.normal(mean=torch.full([10],0),std=torch.arange(1,0,-0.1))

print(b)

print(b.reshape(2,5))


"""
full函数
"""
print("\nfull函数........................")

print(torch.full([2,3],7))

# 生成标量
print(torch.full([],7))

# 生成dim为1的向量
print(torch.full([1],7))


"""
arange函数
"""
print("\narange函数........................")

print(torch.arange(0,10))
print(torch.arange(0.,10.))

print(torch.arange(0,10,2))

# 不推荐使用range
print(torch.range(0,10))

"""
linspace/logspace 生成等分数组
"""
print("\nlinspace/logspace函数........................")

# 包含10 数量为4
print(torch.linspace(0,10,steps=4))

print(torch.linspace(0,10,steps=11))

print(torch.logspace(0,-1,steps=10))

print(torch.logspace(0,1,steps=10))

"""
Ones/zeros/eye
"""
print("\nOnes/zeros/eye函数........................")

print(torch.ones(3,3))

print(torch.zeros(3,3))

# 对角矩阵
print(torch.eye(3,4))
print(torch.eye(3))

c = torch.zeros(3,3)

print(torch.ones_like(c))


"""
randperm 随机打散
"""
print("\nrandperm函数........................")

# 生成0-10 不包含10的最忌索引
print(torch.randperm(10))

d = torch.rand(2,3)
e = torch.rand(2,2)

idx = torch.randperm(2)
print(idx)

print(a[idx])

print(b[idx])

print(a,b)

