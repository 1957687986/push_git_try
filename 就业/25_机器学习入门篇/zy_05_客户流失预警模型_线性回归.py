import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_excel("./data/股票客户流失.xlsx")

# 划分特征变量和目标变量
x = df.drop(columns="是否流失")

y = df["是否流失"]

# 划分训练集与测试集
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=1)

# 模型搭建
model = LogisticRegression()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)
print(y_predict[0:100])

score = accuracy_score(y_predict,y_test)

print(score)

# 模型使用2：预测概率
y_predict_proba = model.predict_proba(x_test)

print(y_predict_proba[0:5])
