import torch
from torch import nn
import  torch.nn.functional as F

# 1 代表输入通道 黑白图片  3代表观察窗口数量  1代表步长  0代表0填充
layer = nn.Conv2d(1,3,kernel_size=3,stride=1,padding=0)
x = torch.rand(1,1,28,28)

out = layer.forward(x)
print(out.shape)

layer = nn.Conv2d(1,3,kernel_size=3,stride=1,padding=1)
out = layer.forward(x)
print(out.shape)

layer = nn.Conv2d(1,3,kernel_size=3,stride=2,padding=1)
out = layer.forward(x)
print(out.shape)

out = layer(x)

print(out.shape)


"""
池化
"""
print("池化..............")
x = out
print(x.shape)
layer = nn.MaxPool2d(2,stride=2)

out = layer(x)
print(out.shape)

out = F.avg_pool2d(x,2,stride=2)
print(out.shape)


"""
激活
"""
print("激活..............")

print(x.shape)
layer = nn.ReLU(inplace=True)

out = layer(x)
print(out.shape)


