import torch


"""
Cat 拼接
"""
print("Cat 拼接....................")

a = torch.rand(4,32,8)

b = torch.rand(5,32,8)

print(torch.cat([a,b],dim=0).shape)

"""
Cat  例子
"""
print("\nCat  例子......................")

a1 = torch.rand(4,3,32,32)
a2 = torch.rand(5,3,32,32)

print(torch.cat([a1,a2],dim=0).shape)

a2 = torch.rand(4,1,32,32)
# 错误
# print(torch.cat([a1,a2],dim=1).shape)

print(torch.cat([a1,a2],dim=1).shape)

a1 = torch.rand(4,3,16,32)
a2 = torch.rand(4,3,16,32)

print(torch.cat([a1,a2],dim=2).shape)


"""
Stack  创建维度
"""
print("\nStack  创建维度......................")

print(torch.stack([a1,a2],dim=2).shape)

a = torch.rand(32,8)

b = torch.rand(32,8)

print(torch.stack([a,b],dim=0).shape)



"""
split  拆分
"""
print("\nsplit   拆分........................")

c = torch.stack([a,b],dim=0)

print(c.shape)

aa,bb = c.split([1,1],dim=0)

print(aa.shape,bb.shape)

# 按长度拆分
aa,bb = c.split(1,dim=0)

print(aa.shape,bb.shape)

# 错误
# 只可拆分为一个不可用两个变量来接受
# aa,bb = c.split(2,dim=0)



"""
chunk  数量拆分
"""
print("\nsplit   数量拆分........................")

print(c.shape)

# 拆分为两个
aa,bb = c.chunk(2,dim=0)

print(aa.shape,bb.shape)
