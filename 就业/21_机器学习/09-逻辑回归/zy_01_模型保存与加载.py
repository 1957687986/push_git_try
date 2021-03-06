from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import joblib

# 获取数据
lb = load_boston()

# 分割数据集到训练集和测试集
x_train,x_test,y_train,y_test = train_test_split(lb.data,lb.target,test_size=0.25)

print(y_train,y_test)

# 进行标准化处理  需要对目标值进行标准化处理
# 特征值和目标值都必须进行标准化处理  --  实例化两个标准化API
std_x = StandardScaler()

x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)

std_y = StandardScaler()

# 版本更新fit_transform传入的必须是二维的
y_train = std_y.fit_transform(y_train.reshape(-1,1))
y_test = std_y.transform(y_test.reshape(-1,1))

# 预测房价结果
model = joblib.load("../tmp/test.pkl")

y_predict = std_y.inverse_transform(model.predict(x_test))

print("保存的模型预测的结果：",y_predict)
