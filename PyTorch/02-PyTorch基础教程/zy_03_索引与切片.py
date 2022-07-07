import torch
import numpy as np

a = torch.rand(4,3,28,28)

print(a[0].shape)

print(a[0,0].shape)

print(a[0,0,2,4])

"""
连续片段
"""
print("\n连续片段..................")

print(a.shape)

print(a[:2].shape)

print(a[:2,:1,:,:].shape)

print(a[:2,1:,:,:].shape)

print(a[:2,-1:,:,:].shape)


"""
间隔片段
"""
print("\n间隔片段....................")

print(a[:,:,0:28:2,0:28:2].shape)

print(a[:,:,::2,::2].shape)


"""
单独采样
"""
print("\n单独采样....................")

# 第0“维度”下的第0个图与第2个图
# torch.Size([2, 3, 28, 28])
print(a.index_select(0,torch.tensor([0,2])).shape)

# 第1“维度”下的第1个通道与第2个通道
# torch.Size([4, 2, 28, 28])
print(a.index_select(1,torch.tensor([1,2])).shape)

# torch.Size([4, 3, 28, 28])
print(a.index_select(2,torch.arange(28)).shape)

# torch.Size([4, 3, 8, 28])
print(a.index_select(2,torch.arange(8)).shape)


"""
...   代表任意多维度
"""
print("\n任意多维度....................")

print(a[...].shape)

print(a[0,...].shape)

print(a[:,1,...].shape)

print(a[...,:2].shape)
