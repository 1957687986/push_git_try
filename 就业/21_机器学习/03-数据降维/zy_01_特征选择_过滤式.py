from sklearn.feature_selection import VarianceThreshold
"""
降维:
1. 维度: 特征的数量，有四个特征即四维
   原因: 数据对最后的目标影响不大

特征选择的原因:
1. 冗余: 部分特征的相关度高，容易消耗计算机性能
2. 噪声: 部分特征对预测结果有影响

过滤式: 通过方差大小，考虑所有样本这个特征的数据情况
"""

def var():
    """
    特征选择 - 删除低方差特征

    :return: None
    """
    var = VarianceThreshold(threshold=1.0)

    data = var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])

    print(data)

    return None

if __name__ == '__main__':
    var()
