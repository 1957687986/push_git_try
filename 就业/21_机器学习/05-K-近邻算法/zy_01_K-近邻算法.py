from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler
import pandas as pd
"""
K-近邻算法公式:
欧式距离: （(a1-b1)^2 + (a2-b2)^2 + (a3-b3)^2）开方

需要标准化!!!

算法流程
1. 调用fit   fit(x_train,y_train)  为了输入算法当中
2. 输入测试集数据
3. 评估
"""

def knncls():
    """
    K-近邻预测用户签到位置
    :return: None
    """
    file_path1 = "./train.csv"
    file_path2 = ""

    # 读取数据
    data = pd.read_csv(open(file_path1))

    # print(data.head(10))

    # 处理数据!!!
    # 1. 缩小数据,查询数据，筛选数据 data 格式是DataFrame
    data = data.query("x > 1.0 & x < 1.3 & y > 2.5 & y < 2.8")

    # 2. 处理时间数据
    time_value = pd.to_datetime(data["time"],unit="s")

    # print(time_value)

    # 把日期格式转换成字典格式
    time_value = pd.DatetimeIndex(time_value)

    # 构造一些特征
    data["day"] = time_value.day
    data["hour"] = time_value.hour
    data["weekday"] = time_value.weekday

    # 把时间戳特征删除  sklearn中axis = 1表示列
    data = data.drop(["time"],axis=1)
    print(data)

    # 把签到数量少于n个目标位置删除
    place_count = data.groupby(by="place_id").count()

    # reset_index 是将place_id设置为索引，成为单独的一列
    tf = place_count[place_count.row_id > 3].reset_index()

    data = data[data["place_id"].isin(tf.place_id)]

    # 取出数据当中的特征值与目标值
    y = data["place_id"]
    x = data.drop(["place_id"],axis=1)

    # 进行数据分割为数据集与测试集
    x_train , x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.25)

    # 特征工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=5)

    # fit predict score
    knn.fit(x_train,y_train)

    # 得出预测结果
    y_predict = knn.predict(x_test)

    print("预测目标签到位置为：",y_predict)

    # 得出准确率
    print("预测准确率：",knn.score(x_test,y_test))

    return None


if __name__ == '__main__':
    knncls()