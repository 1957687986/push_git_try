from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler
import pandas as pd


def iris():
    # 获取数据
    file_path = "./iris.csv"

    data = pd.read_csv(file_path)

    print(data.head(5))

    # 取出数据当中的特征值与目标值
    y = data["Species"]
    x = data.drop(["Species"], axis=1)

    # 进行数据分割为数据集与测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程（标准化）
    # 先实例化
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=5)

    # fit predict score
    knn.fit(x_train, y_train)

    # 得出预测结果
    y_predict = knn.predict(x_test)

    print("预测目标：", y_predict)

    # 得出准确率
    print("预测准确率：", knn.score(x_test, y_test))

    return None


if __name__ == '__main__':
    iris()