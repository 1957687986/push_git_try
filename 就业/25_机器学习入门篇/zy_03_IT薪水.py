import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("./data/IT行业收入表.xlsx")

x = df[["工龄"]]

y = df[["薪水"]]

plt.rcParams["font.sans-serif"] = ["SimHei"]

plt.scatter(x,y)

plt.xlabel("工龄")

plt.ylabel("薪水")

plt.show()

regr = LinearRegression()

regr.fit(x,y)

plt.scatter(x,y)

plt.plot(x,regr.predict(x),color = "red")

plt.xlabel("工龄")

plt.ylabel("薪水")

plt.show()

print("系数a:"+ str(regr.coef_[0]))

print("截距b:"+ str(regr.intercept_))

