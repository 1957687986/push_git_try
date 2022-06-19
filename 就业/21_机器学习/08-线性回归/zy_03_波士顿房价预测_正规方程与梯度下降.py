from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

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
    # 正规方程求解方式预测结果
    lr = LinearRegression()

    lr.fit(x_train,y_train)

    print("正规方程回归系数：",lr.coef_)

    # 预测测试集的价格
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))

    print("正规方程测试集中每个房子的价格：",y_lr_predict)

    print("正规方程的均方误差：",mean_squared_error(std_y.inverse_transform(y_test),y_lr_predict))


    # 梯度下降回归优化
    sgd = SGDRegressor()

    sgd.fit(x_train, y_train)

    print("梯度下降回归系数：", sgd.coef_)

    # 预测测试集的价格
    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))

    print("梯度下降测试集中每个房子的价格：", y_sgd_predict)

    print("梯度下降的均方误差：",mean_squared_error(std_y.inverse_transform(y_test),y_sgd_predict))


if __name__ == '__main__':
    mylinear()