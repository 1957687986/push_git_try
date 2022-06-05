import pandas as pd
# 特征抽取API  --->  one_hot编码
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier


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
    # dict抽取完的结果：['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male']
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))

    print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient="records"))

    print(x_train)

    # 用随机森林进行预测 （超参数调优）
    rf = RandomForestClassifier()

    param = {"n_estimators":[120,200,300,500,800,1200],"max_depth":[5,8,15,25,30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf,param_grid=param,cv=5)

    gc.fit(x_train,y_train)

    print("预测准确率为：",gc.score(x_test,y_test))

    print("查看选择的参数模型：",gc.best_params_)

    return None


if __name__ == '__main__':
    decision()
