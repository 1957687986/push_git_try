from sklearn.preprocessing import MinMaxScaler

"""
公式：
_x1 = (x-min)/(max-min)
_x2 = _x1*(mx-mi)+mi
ma,mi分别为指定区间值，默认ma为1，mi为0
"""

def Mm():
    """
    归一化处理:
    为了使某一个特征不会对你的判断造成更大的影响
    缺点:
    对异常点处理不好
    应用场景:
    适合传统精确小数据（很少）
    :return: None
    """
    mm = MinMaxScaler(feature_range=(2,3))

    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])

    print(data)

    return None

if __name__ == '__main__':
    Mm()