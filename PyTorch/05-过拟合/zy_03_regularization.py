import torch
import  torch.nn as nn
from torch import optim

batch_size=200
learning_rate=0.01
epochs=10

class MLP(nn.Module):

    def __init__(self):
        super(MLP, self).__init__()

        # 定义网络的每一层，nn.ReLU可以换成其他激活函数，比如nn.LeakyReLU()
        self.model = nn.Sequential(
            nn.Linear(784, 200),
            nn.ReLU(inplace=True),
            nn.Linear(200, 200),
            nn.ReLU(inplace=True),
            nn.Linear(200, 10),
            nn.ReLU(inplace=True),
        )


device = torch.device('cuda:0')

net = MLP().to(device)

optimizer = optim.SGD(net.parameters(),lr=learning_rate,weight_decay=0.01)

criteon = nn.CrossEntropyLoss().to(device)