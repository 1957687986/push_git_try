from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

lb = load_boston()

print("获取特征值")
print(lb.data)
print("获取目标值")
print(lb.target)
print("获取属性")
print(lb.DESCR)
