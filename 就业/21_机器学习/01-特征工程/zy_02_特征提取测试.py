from sklearn.feature_extraction import DictVectorizer

def dictvec():
    """
    字典数据抽取  :  把字典数据中一些类别数据，分别进行转化成特征
    数组形式：有类别特征，先要转换成字典数据
    :return: None
    """
    # 实例化
    # dict = DictVectorizer()
    dict = DictVectorizer(sparse=False)

    # 调用fit_transform
    data = dict.fit_transform([{'city' : '北京','temperature': 100},
                        {'city' : '上海','temperature': 60},
                        {'city' : '深圳','temperature': 30}])

    print(dict.get_feature_names())

    print(dict.inverse_transform(data))

    print(data)

    return None

if __name__ == '__main__':
    dictvec()

    """
    (0, 1)	1.0
    (0, 3)	100.0
    (1, 0)	1.0
    (1, 3)	60.0             ====>[[  0.   1.   0. 100.]
    (2, 2)	1.0                    [  1.   0.   0.  60.]
    (2, 3)	30.0                   [  0.   0.   1.  30.]]
    
    sparse 矩阵 
    """
