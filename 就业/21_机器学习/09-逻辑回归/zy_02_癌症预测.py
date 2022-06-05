import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

"""
逻辑回归 适用于二分类

特点：也可以得出概率值
"""

def logisitic():
    """
    逻辑回归做二分类进行癌症预测（根据细胞的属性特征）
    :return: None
    """
    # 构造列标签名字
    column = ['Sample code number','Clump Thickness', 'Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion', 'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",names=column)

    print(data)

    # 缺失值进行处理
    data = data.replace(to_replace="?",value=np.nan)

    data = data.dropna()

    # 进行数据的分割
    x_train,x_test,y_train,y_test = train_test_split(data[column[1:-1]],data[column[-1]],test_size=0.25)

    # 标准化   x 为特征值 y 为目标值
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归
    log = LogisticRegression(C=1.0)

    log.fit(x_train,y_train)

    print(log.coef_)

    y_predict = log.predict(x_test)

    print("准确率：",log.score(x_test,y_test))

    print("召回率：",classification_report(y_test,y_predict,labels=[2,4],target_names=["良性","恶性"]))

    return None

if __name__ == '__main__':
    logisitic()