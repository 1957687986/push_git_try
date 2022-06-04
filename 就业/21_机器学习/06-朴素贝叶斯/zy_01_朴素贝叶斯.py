from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import  classification_report

"""
常用于文本分类
"""

def Naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    news = fetch_20newsgroups(subset="all")
    # print(news.data)
    # print(news.target)

    # 进行数据分割  特征值、目标值、测试集大小
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计
    x_train = tf.fit_transform(x_train)

    print(tf.get_feature_names())

    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法
    mlt = MultinomialNB(alpha=1.0)

    print(x_train)

    mlt.fit(x_train,y_train)

    y_predict = mlt.predict(x_test)

    print("文章类别预测值",y_predict)

    print("准确率：",mlt.score(x_test,y_test))

    print("每个类别的精确率与召回率",classification_report(y_test,y_predict,target_names=news.target_names))

    return None


if __name__ == '__main__':
    Naviebayes()