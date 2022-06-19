import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_excel("./data/客户价值数据表.xlsx")

print(df.head(5))

print(df.shape)

x = df[["历史贷款金额","贷款次数","学历","月收入","性别"]]
y = df["客户价值"]

regr = LinearRegression()
regr.fit(x, y)

print("各系数："+str(regr.coef_))
print("常系数K0："+ str(regr.intercept_))

x2 = sm.add_constant(x)

est = sm.OLS(y,x2).fit()
print(est.summary())
