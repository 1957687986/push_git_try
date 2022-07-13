import torch
# 多线程加载数据API
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from torch import nn,optim

from lenet import Lenet5

def main():
    batch_size = 32

    cifar_train = datasets.CIFAR10('cifar',True,transform=transforms.Compose([
        transforms.Resize((32,32)),
        transforms.ToTensor(),
    ]),download=True)
    # shuffle  ==>  随机化
    cifar_train = DataLoader(cifar_train, batch_size=batch_size,shuffle=True)

    cifar_test = datasets.CIFAR10('cifar', False, transform=transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
    ]), download=True)
    # shuffle  ==>  随机化
    cifar_test = DataLoader(cifar_test, batch_size=batch_size, shuffle=True)

    # 加载一点数据进行观察
    x, label = iter(cifar_train).__next__()
    print("x:",x.shape,"label:",label.shape)

    device = torch.device("cpu")
    model = Lenet5().to(device)
    criteon = nn.CrossEntropyLoss().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    print(model)

    for epoch in range(1000):
        for batchidx, (x, label) in enumerate(cifar_train):
            # [b, 3, 32, 32]
            # [b]
            x, label = x.to(device), label.to(device)

            logits = model(x)
            # logits: [b, 10]
            # label:[b]
            # loss tensor scalar
            loss = criteon(logits, label)

            # backprop
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(epoch,loss.item())

        # test
        for x,label in cifar_test:
            # [b, 3, 32, 32]
            # [b]
            x, label = x.to(device), label.to(device)

            # [b,10]
            logits = model(x)




if __name__ == '__main__':
    main()
