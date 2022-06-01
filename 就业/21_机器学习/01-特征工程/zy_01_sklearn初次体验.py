import sklearn
# sklearn.feature_extraction特征抽取
from sklearn.feature_extraction.text import CountVectorizer

"""
字典数据特征抽取
sklearn.feature_extraction.DictVectorizer

语法：
DictVectorizer.fit_transfrom(x)
x为字典或者包含字典的迭代器
返回值：返回sparse矩阵

"""

vector = CountVectorizer()

res = vector.fit_transform(["life is short,i like python","life is too long,i dislike python"])

# 打印结果
print(vector.get_feature_names())
print(res.toarray())
