import numpy as np
import torch


"""
从numpy中导入tensor数组
"""
print("从numpy中导入tensor数组............")
a = np.array([2,3.3])

print(a)

print(torch.from_numpy(a))

b = np.ones([2,3])

print(b)

print(torch.from_numpy(b))

"""
从list中导入

对于tensor()括号中接受现成的数据
对于FloatTensor()括号中接受现成数据或shape 数据的形状  维度
"""
print("从list中导入......................")

print(torch.tensor([2,3.2]))

print(torch.FloatTensor([2.,3.2]))
print(torch.FloatTensor(1,2,3))

print(torch.tensor([[2.,3.2],[1.,22.3]]))


"""
生成未初始化的数据  需要对未初始化的数据进行覆盖
"""
print("生成未初始化的数据......................")

print(torch.empty([2,3]))

print(torch.empty(1))

print(torch.Tensor(2,3))

print(torch.IntTensor(2,3))

print(torch.FloatTensor(2,3))

"""
设置默认数据类型
"""
print("设置默认数据类型......................")

print(torch.tensor([1.2,3]).type())
print(torch.Tensor([1,3]).type())

torch.set_default_tensor_type(torch.DoubleTensor)

print(torch.tensor([1.2,3]).type())
