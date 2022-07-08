import torch

"""
statistics   norm   在某一维上所有元素平方求和，开次方
"""

a = torch.full([8],1)

b = a.view(2,4)

c = a.view(2,2,2)

print(b)

print(c)

print(a.norm(1),b.norm(1),c.norm(1))

print(a.norm(2),b.norm(2),c.norm(2))

print(b.norm(1,dim=1))

print(b.norm(2,dim=1))

print(c.norm(1,dim=0))

print(c.norm(2,dim=0))



"""
统计属性
"""
print("\n统计属性.........................")

a = torch.arange(8).view(2,4).float()

print(a)

print(a.min(),a.max(),a.mean(),a.prod())

print(a.sum())

print(a.argmax(),a.argmin())

a  =a.view(1,2,4)

print(a.argmax())

print(a.argmin())

a = torch.rand(2,3,4)

print(a.argmax())

a = torch.randn(4,10)

print(a[0])

print(a.argmax())

print(a.argmax(dim=1))



"""
dim 与 keepdim
"""
print("\ndim 与 keepdim.........................")
print(a)

print(a.max(dim=1))

print(a.argmax(dim=1))

print(a.max(dim=1,keepdim=True))

print(a.argmax(dim=1,keepdim=True))



"""
Top-k
"""
print("\nTop-k.........................")

print(a.topk(3,dim=1))

print(a.topk(3,dim=1,largest=False))

# 第八小
print(a.kthvalue(8,dim=1))

print(a.kthvalue(3))

print(a.kthvalue(3,dim=1))



"""
比较运算
"""
print("\n比较运算.........................")

print(a>0)

print(torch.gt(a,0))

print(a!=0)

a = torch.ones(2,3)
b = torch.randn(2,3)

# 比较是否相等
print(torch.eq(a,b))

print(torch.eq(a,a))

# 比较是否完全一样
print(torch.equal(a,a))

