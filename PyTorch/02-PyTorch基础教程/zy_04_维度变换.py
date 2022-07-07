import torch

"""
变换形状
"""
print("变换形状........................")

a = torch.rand(4,1,28,28)

print(a.shape)

print(a.view(4,28*28))

print(a.view(4,28*28).shape)

print(a.view(4*1,28,28).shape)

b = a.view(4,28*28)

print(b.view(4,28,28,1))



"""
挤压   squeeze      展开  unsqueeze
"""
print("\n展开........增加维度....................")

print(a.unsqueeze(0).shape)

print(a.unsqueeze(-1).shape)

print(a.unsqueeze(4).shape)

print(a.unsqueeze(-4).shape)

print(a.unsqueeze(-5).shape)

# 错误
# print(a.unsqueeze(5).shape)


print("\n案例........................")
b = torch.rand(32)

f = torch.rand(4,32,14,14)

b = b.unsqueeze(1).unsqueeze(2).unsqueeze(0)

print(b.shape)

print("\n维度删减...........................")

print(b.squeeze().shape)

print(b.squeeze(0).shape)

print(b.squeeze(-1).shape)

# 维度1上的数据不是1 不可挤压
# torch.Size([1, 32, 1, 1])
print(b.squeeze(1).shape)

print(b.squeeze(-4).shape)


"""
维度扩展 expand
"""
print("\n纬度扩展...........................")

a = torch.rand(4,32,14,14)

print(b.expand(4,32,14,14).shape)

print(b.expand(-1,32,-1,-1).shape)

print(b.expand(-1,32,-1,-4).shape)


"""
维度扩展 repeat
"""
print("\nrepeat..........................")

print(b.repeat(4,32,1,1).shape)

print(b.repeat(4,1,1,1))

print(b.repeat(4,1,32,32))


"""
矩阵转置
"""
print("\n矩阵转置.........................")

c = torch.randn(3,4)

print(c.t())


"""
维度交换
"""
print("\n维度交换 Transpose......................")

print(b.transpose(1,2).shape)

# 错误
# a1 = a.transpose(1,3).contiguous().view(4,3*32*32).view(4,3,32,32)
#
# a2 = a.transpose(1,3).contiguous().view(4,3*32*32).view(4,32,32,3).transpose(1,3)
#
# print(a1.shape,a2.shape)
#
# print(torch.all(torch.eq(a,a1)))
#
# print(torch.all(torch.eq(a,a2)))


"""
premute............
"""
print("premute............")
a = torch.rand(4,3,28,28)

print(a.transpose(1,3).shape)

b = torch.randn(4,3,28,32)

print(b.transpose(1,3).shape)

print(b.transpose(1,3).transpose(1,2).shape)

# 直接放置维度
print(b.permute(0,2,3,1))
