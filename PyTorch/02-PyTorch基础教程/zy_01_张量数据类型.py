import torch
import numpy as np

"""
dim指的是数据维度
size或shape指的是整体维度(形状)  [2,2]

tensor指的是具体的数据     [1,2]
                        [3,4]
"""



"""
randn为随机初始化正态分布均值为0，方差为1  即 N(0,1)   的随机数据
randn(2,3)为两行三列
"""
a = torch.randn(2,3)

print(a.type())

print(type(a))

print(isinstance(a,torch.FloatTensor))

print(torch.tensor(1.))
print(torch.tensor(1.3))

"""
dim为0的标量
"""
print("-"*7+"下面是dim为0的标量"+"-"*7)
b = torch.tensor(2.2)
print(b.shape)

print(len(b.shape))

print(b.size())

"""
dim为1的向量  ===>  一般用于神经元的bias   或线性层输入
"""
print("-"*7+"下面是dim为1的向量"+"-"*7)
c = torch.tensor([1.1])
print(c)

d = torch.tensor([1.1,2.2])
print(d)

"""
第一个size为1，即向量中只包含一个数据
第一个size为2，即向量中只包含两个数据
"""
print(torch.FloatTensor(1))

print(torch.FloatTensor(2))

data = np.ones(2)
print(data,data.dtype)

print(torch.from_numpy(data))

e = torch.ones(2)
print(a.shape)

"""
dim为2
"""
print("-"*7+"下面是dim为2的向量"+"-"*7)

f = torch.randn(2,3)
print(f)

print(f.shape)

# 取size的第一个维度  ==> [10,20]  size(0)指的是第一位10  size(1)指的是第二位20

print(f.size(0))
print(f.size(1))

print(f[0])

# shape与size一致
print(a.shape[1])

"""
dim为3
"""
print("-"*7+"下面是dim为3的向量"+"-"*7)


# rand为均匀分布

g = torch.rand(1,2,3)
print(g)
g1 = torch.rand(2,2,3)
print(g1)

print(g.shape)


# 取第1个元素“1”得到[2,3]  第一个维度的第0个元素

print(g[0])

print(list(g.shape))


"""
dim为4   适合于图像处理
"""
print("-"*7+"下面是dim为4的向量"+"-"*7)

h = torch.rand(2,3,28,28)
print(h)

print(h.shape)

# numel = 2*3*28*28 = 4708  占用内存
print(h.numel())

print(h.dim())

i = torch.tensor(1)
print(i.dim())

