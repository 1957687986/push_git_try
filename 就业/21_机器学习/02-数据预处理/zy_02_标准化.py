from sklearn.preprocessing import StandardScaler

"""
公式：
_x1 = (x-mean)/(标准差）
_x2 = _x1*(mx-mi)+mi
mean为平均值
作用于每一列
方差：
var = （(x1-mean)平方+(x2-mean)平方+(x3-mean)平方） /  m(样本数 也就是多少行）
标准差 = var开平方
StandardScaler 处理之后对每列来说，所有数据都聚集在均值为0附近标准差为1
 1.33630621 ,-0.26726124,-1.06904497  这三个标准差和为0
"""

def stand():
    """
    标准化缩放:
    为了使某一个特征不会对你的判断造成更大的影响
    缺点:
    应用场景:
    在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景
    :return: None
    """
    mm = StandardScaler()

    data = mm.fit_transform([[1,-1,3],[2,4,2],[4,6,-1]])

    print(data)

    return None

if __name__ == '__main__':
    stand()
