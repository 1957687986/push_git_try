from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

def CutWord():
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")

    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")

    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")

    # 由生成器转换为列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    # print(content1)
    # ['今天', '很', '残酷', '，', '明天', '更', '残酷', '，', '后天', '很', '美好', '，', '但', '绝对', '大部分', '是', '死', ]

    # 把列表转换为字符串
    c1 = ' '.join(content1)
    # 今天 很 残酷 ， 明天 更 残酷 ， 后天 很 美好 ， 但 绝对 大部分 是 死 在 明天 晚上 ， 所以 每个 人 不要 放弃 今天 。
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1,c2,c3


def Tfidfvec():
    """
    中文特征值化
    :return: None
    """
    c1,c2,c3 = CutWord()
    print(c1,c2,c3)

    # 得到的数据反应一个词组的重要性
    tf = TfidfVectorizer()

    # fit_transform(raw_documents, y=None):学习词汇词典并返回术语 - 文档矩阵(稀疏矩阵)。
    data = tf.fit_transform([c1,c2,c3])

    print(tf.get_feature_names())

    print(data.toarray())

    return None


if __name__ == '__main__':
    Tfidfvec()