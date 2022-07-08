import torch


"""
数学运算   basic
"""
print("basic..................................")

a = torch.rand(3,4)

b = torch.rand(4)

print(a+b)

print(torch.add(a,b))

# 检查运算符号与函数运算是否一致
print(torch.all(torch.eq(a-b,torch.sub(a,b))))

print(torch.all(torch.eq(a*b,torch.mul(a,b))))

print(torch.all(torch.eq(a/b,torch.div(a,b))))



"""
数学运算   矩阵相乘
"""
print("\n矩阵相乘..................................")


a = torch.tensor([3.,3.,3.,3.])
a = a.reshape([2,2])
print(a)

b = torch.ones(2,2)

# 只适合于2d，不推荐
print(torch.mm(a,b))

print(torch.matmul(a,b))

print(a@b)


"""
矩阵相乘 2维 例子
"""
print("\n矩阵相乘  2维  例子.....................")

a = torch.rand(4,784)

x = torch.rand(4,784)

# pytorch写法  第一个数为输出维度，第二个数为输入维度
w = torch.rand(512,784)

# 所以在此用  .t()  进行转置  仅对二维  如果是高维需要transpose
print((x@w.t()).shape)



"""
矩阵相乘 高维 例子
"""
print("\n矩阵相乘  高维  例子.....................")

a = torch.rand(4,3,28,64)

b = torch.rand(4,3,64,32)

print(torch.matmul(a,b).shape)

b = torch.rand(4,1,64,32)

print(torch.matmul(a,b).shape)

# b = torch.rand(4,62,32)
# 错误
# print(torch.matmul(a,b).shape)



"""
次方运算    power
"""
print("\n次方运算  power.....................")

a = torch.full([2,2],3)

print(a.pow(2))

print(a**2)

aa = a**2

print(aa.sqrt())

# 倒数
print(aa.rsqrt())

# 开方
print(aa**(0.5))



"""
exp 与 log
"""
print("\nexp 与 log.....................")

a = torch.exp(torch.ones(2,2))

print(a)

print(torch.log(a))



"""
近似值
"""
print("\n近似值.....................")

a = torch.tensor(3.14)

print(a.floor(),a.ceil(),a.trunc(),a.frac())

a = torch.tensor(3.499)

print(a.round())

a = torch.tensor(3.5)

print(a.round())



"""
裁剪  clamp
"""
print("\n裁剪  clamp.....................")

grad = torch.rand(2,3)*15

print(grad.max())

print(grad.median())

print(grad.clamp(10))

print(grad)

print(grad.clamp(0,10))
