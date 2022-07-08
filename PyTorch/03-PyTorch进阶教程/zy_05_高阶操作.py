import torch

"""
where    torch.where(condition,x,y)
"""
print("where............................")

cond = torch.tensor([[0.6,0.7],
                     [0.8,0.4]])

a = torch.zeros([2,2])
# print(a)
b = torch.ones([2,2])

print(torch.where(cond>0.5,a,b))




"""
gather   torch.gather(input,dim,index,out=None)
"""
print("gather............................")

prob = torch.randn(4,10)

idx = prob.topk(dim=1,k=3)

idx = idx[1]

label = torch.arange(10) + 100

print(label)

print(torch.gather(label.expand(4,10),dim=1,index=idx.long()))
