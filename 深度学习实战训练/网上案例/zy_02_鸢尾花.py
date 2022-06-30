import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = pd.read_csv('../data/iris_training.csv')
x = iris.values[:, 0:4]
y = iris.values[:, 4]  # 读取数据，分为数据和索引

x = x / 8 * 0.99 + 0.01  # 归一化数据


def sigmiod(X):
    return 1 / (1 + np.exp(-X))  # 定义激活函数


x_train, x_test, y_train, y_test = train_test_split(x, y)  # 划分训练集和测试集

oneHot = np.identity(3)
for i in range(oneHot.shape[0]):
    for j in range(oneHot.shape[1]):
        if (oneHot[i, j] == 1):
            oneHot[i, j] = 0.99
        else:
            oneHot[i, j] = 0.01
y_true = oneHot[y_train.astype(int)]  # oneHot编码函数，网上有介绍

eta = 0.01  # 学习率
w1 = np.random.normal(0.0, 1, (4, 8))
w2 = np.random.normal(0.0, 1, (8, 3))  # 定义权重

for i in range(1000):
    result1 = np.dot(x_train, w1)
    result_act1 = sigmiod(result1)
    result2 = np.dot(result_act1, w2)
    result_act2 = sigmiod(result2)  # 训练一千次，正向传播

    error = y_true - result_act2
    error_h = np.dot(error, w2.T)  # 定义损失

    w2_h = np.dot(result_act1.T, -error * result_act2 * (1 - result_act2))
    w1_h = np.dot(x_train.T, -error_h * result_act1 * (1 - result_act1))

    w2 -= w2_h * eta
    w1 -= w1_h * eta  # 反向传播和训练权重

result3 = np.dot(x_test, w1)
result_act3 = sigmiod(result3)
result4 = np.dot(result_act3, w2)
result_act4 = sigmiod(result4)  # 利用测试集测试

acc = []
for i in range(result_act4.shape[0]):
    acc.append(np.argmax(result_act4[i]))
acc = np.array(acc)
accuracy_score(y_test, acc)
print('acc=', accuracy_score(y_test, acc))  # 计算准确率
