#导入包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

#1.加载糖尿病数据,观察数据
data_diabetes=load_diabetes()
#print(data_diabetes)
data=data_diabetes['data']
target=data_diabetes['target']
feature_names=data_diabetes['feature_names']
#一维数据形式，将她们组合成dataframe，可以更直观地观察数据
df = pd.DataFrame(data, columns=feature_names)
print("查看前几行数据\n",df.head())  # 查看前几行数据
# 查看数据集的基本信息
print("以上是查看的数据集基本信息\n",df.info())

temp_X=data[:, np.newaxis, 2]#获取一个特征
train_X=temp_X[:221]#训练样本
test_X=temp_X[221:]#测试样本
train_y=target[:221]#训练标记
test_y=target[221:]#测试标记

model=LinearRegression()
model.fit(train_X,train_y)

print("Coefficient(系数):%.2f" %model.coef_)
print("Residual sum of square(残差平方和):%.2f" %np.mean((model.predict(test_X) - test_y) ** 2))
print("variance score(方差得分): %.2f" %model.score(test_X, test_y))


'''
5.考察每个特征值与结果之间的关系，分别以散点图展示。

思考：根据散点图结果对比，哪个特征值与结果之间的相关性最高？
'''
#绘图
plt.title('LinearRegression Diabetes')   #标题(糖尿病回归模型)
plt.xlabel(u'Attributes')                 #x轴坐标(属性)
plt.ylabel(u'Measure of disease')         #y轴坐标(疾病测量)
#点的准确位置
plt.scatter(test_X,test_y, color = 'red')
#预测结果 直线表示
plt.plot(test_X, model.predict(test_X), color='blue', linewidth = 3)
plt.show()

