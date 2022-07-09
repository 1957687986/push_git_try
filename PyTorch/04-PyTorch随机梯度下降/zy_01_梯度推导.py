import torch
from torch.nn import functional as F

a =  torch.linspace(-1,1,10)

print(torch.tanh(a))

print(torch.relu(a))

print(F.relu(a))


x = torch.ones(1)

w = torch.full([1],2)

mse = F.mse_loss(torch.ones(1),x*w)

print(mse)

# print(torch.autograd.grad(mse,[w]))

print(w.requires_grad_())

# print(torch.autograd.grad(mse,[w]))

mse = F.mse_loss(torch.ones(1),x*w)

print(torch.autograd.grad(mse,[w]))

# mse.backward()

print(w.grad)

a = torch.rand(3)

print(a.requires_grad_())

p = F.softmax(a,dim=0)

# p.backward()

print(torch.autograd.grad(p[1],[a],retain_graph=True))

print(torch.autograd.grad(p[2],[a]))

