import pandas as pd
# 特征抽取API  --->  one_hot编码
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import DecisionTreeClassifier,export_graphviz

def decision():
    """
    决策树对泰坦尼克号预测生死
    :return: None
    """
    file_path = "./titanic.csv"
    titan = pd.read_csv(file_path)

    print(titan.head(5))
    print(titan.info())
    # 处理数据，找出特征值，目标值
    x = titan[["pclass","age","sex"]]

    y = titan["survived"]

    print(x)

    # 缺失值处理
    x["age"].fillna(x["age"].mean(),inplace=True)

    # 分割数据集到训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

    # 进行处理（特征工程）特征 -> 为类别 -> one_hot编码
    dict = DictVectorizer(sparse=False)
    # x_train.to_dict(orient="records") -- pd转换字典，特征抽取
    # ['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male']
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))

    print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient="records"))

    print(x_train)

    # 用决策树进行预测
    dec = DecisionTreeClassifier(max_depth=5)

    dec.fit(x_train,y_train)

    # 预测准确率
    print("预测准确率：",dec.score(x_test,y_test))

    # 导出决策树的结构
    # export_graphviz(dec,out_file="./tree.dot",feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=女性', 'sex=男性'])

    return None


if __name__ == '__main__':
    decision()