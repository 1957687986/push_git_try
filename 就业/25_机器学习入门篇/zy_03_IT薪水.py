import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 读取数据
df = pd.read_excel("./data/IT行业收入表.xlsx")

x = df[["工龄"]]

y = df[["薪水"]]

plt.rcParams["font.sans-serif"] = ["SimHei"]

plt.scatter(x,y)

plt.xlabel("工龄")

plt.ylabel("薪水")

plt.show()

# 模型搭建
regr = LinearRegression()

regr.fit(x,y)

plt.scatter(x,y)

plt.plot(x,regr.predict(x),color = "red")

plt.xlabel("工龄")

plt.ylabel("薪水")

plt.show()

# 线性回归方程构造
print("系数a:"+ str(regr.coef_[0]))

print("截距b:"+ str(regr.intercept_))

print("-"*100)


# 多元方程
# 设置最高次项为二次项
poly_reg = PolynomialFeatures(degree=2)

# 将代码中原有的x转换为新的二维数组x_
x_ = poly_reg.fit_transform(x)

regr = LinearRegression()

regr.fit(x_,y)

plt.scatter(x,y)

plt.plot(x,regr.predict(x_),color="red")

plt.show()

# 获取相关系数a,b
print(regr.coef_)
# 获取常数c
print(regr.intercept_)

