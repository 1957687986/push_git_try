from sklearn.impute import SimpleImputer
import numpy as np

"""
思想:
1. 删除（不建议）
2. 插补:
   平均值，中位数  一般按列去填补

"""

def Im():
    """
    缺失值处理
    :return:None
    """
    # NaN  /  nan  都可
    im = SimpleImputer(missing_values=np.nan , strategy='mean')
    x1 = np.array([[1,2], [np.nan,3], [7,6]])

    data = im.fit_transform(x1)

    print(data)

    # X1 = np.array([[1, 2, np.nan],
    #                [4, np.nan, 6],
    #                [np.nan, 8, 9]])
    # imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    # print(imp.fit_transform(X1))

    return None

if __name__ == '__main__':
    Im()
