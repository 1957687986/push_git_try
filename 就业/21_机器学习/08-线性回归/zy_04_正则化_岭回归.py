from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
# 模型保存
import joblib


def mylinear():
    """
    线性回归直接预测房子价格
    :return: None
    """
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

    # estimator预测
    # 岭回归求解方式预测结果
    rid = Ridge(alpha=0.5)

    rid.fit(x_train, y_train)

    print("岭回归 回归系数：", rid.coef_)

    # 预测测试集的价格
    y_rid_predict = std_y.inverse_transform(rid.predict(x_test))

    print("岭回归测试集中每个房子的价格：", y_rid_predict)

    print("岭回归的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_rid_predict))

    # 模型保存
    joblib.dump(rid,"../tmp/test.pkl")


if __name__ == '__main__':
    mylinear()