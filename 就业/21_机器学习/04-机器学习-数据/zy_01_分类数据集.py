from sklearn.datasets import load_iris,fetch_20newsgroups
from sklearn.model_selection import train_test_split

li = load_iris()

# print("获取特征值")
# print(li.data)
# print("获取目标值")
# print(li.target)
# print("获取属性")
# print(li.DESCR)

# 返回值包含训练集和测试集
# x_train 训练集中的特征值 ,  y_train 训练集中的目标值
# x_test  测试集中的特征值 ,  y_test  测试集中的目标值
# x_train,x_test,y_train,y_test = train_test_split(li.data,li.target,test_size=0.25)

# print("训练集的特征值和目标值：",x_train,y_train)
# print("测试集的特征值和目标值：",x_test,y_test)

# 获取新闻数据集
news = fetch_20newsgroups(subset="all")

print(news.data)
print(news.target)
