import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = "LogReg_data.txt"

Data = pd.read_csv(path,header=None,names=["Exam 1","Exam 2","Admitted"])

print(Data.head(5))

print(Data.shape)

# 将1 和 0数据分开
positive = Data[Data["Admitted"] == 1]
negative = Data[Data["Admitted"] == 0]

fig, ax = plt.subplots(figsize=(28,10))

ax.scatter(positive["Exam 1"], positive["Exam 2"], s=30, c="b", marker="o", label="Admitted")
ax.scatter(negative["Exam 1"], negative["Exam 2"], s=30, c="r", marker="x", label="Not Admitted")

# 添加图例
ax.legend()

ax.set_xlabel("Exam 1 Score")

ax.set_ylabel("Exam 2 Score")

plt.show()

def sigmoid(z):
    return 1/(1+np.exp(-z))

nums = np.arange(-10,10,step=1)

ax.plot(nums, sigmoid(nums),"r")

def model(x,theta):
    return sigmoid(np.dot(x,theta.T))

Data.insert(0, "Ones", 1)

orig_data = Data.as_matrix()
cols = orig_data.shape()

x = orig_data[:,0:cols-1]
y = orig_data[:,cols-1:cols]

theta = np.zeros([1, 3])

def cost(x,y,theta):
    left = np.multiply(-y,np.log(model(x,theta)))
    right = np.multiply(1 - y,np.log(1-model(x,theta)))
    return np.sum(left-right)

cost(x,y,theta)

