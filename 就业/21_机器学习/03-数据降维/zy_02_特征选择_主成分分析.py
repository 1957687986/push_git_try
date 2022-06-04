from sklearn.decomposition import PCA
"""
主成分分析目的：对数据维数压缩，尽可能降低原数据的维数（复杂度），损失少量信息
作用：可以削减回归分析或者聚类分析中特征的数量

PCA: 特征数量达到上百的时候，考虑数据简化问题  
数据会改变，特征数量会减少
n_components: 
可以是小数: 百分比（90% - 95%）
整数: 减少到的特征数量

"""

def pca():
    """
    主成分分析进行特征降维

    :return: None
    """
    pca = PCA(n_components=0.9)

    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)

    return None

if __name__ == '__main__':
    pca()
