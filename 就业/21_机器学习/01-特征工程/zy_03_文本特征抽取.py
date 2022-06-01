from sklearn.feature_extraction.text import CountVectorizer
import jieba

def Countvec():
    """
    对文本进行特征值化
    工作步骤：
    1. 统计所有文章当中所有的词，重复的只统计一次
    2. 对每篇text，在词的列表里面进行统计没歌词出现的次数
    单个字母不统计
    :return: None
    """

    # 实例化
    cv = CountVectorizer()
    # cv = CountVectorizer(sparse=False)

    # 调用fit_transform
    # data = cv.fit_transform(["life is short,i like python",
    #                   "life is too long,i dislike python"])
    data = cv.fit_transform(["人生苦短，我喜欢python",
                             "人生漫长，我不喜欢python"])

    print(cv.get_feature_names())
    # toarray -- 把sparse矩阵转换成数组
    print(data.toarray())

    return None


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


def Hanzivec():
    """
    中文特征值化
    :return: None
    """
    c1,c2,c3 = CutWord()
    print(c1,c2,c3)

    cv = CountVectorizer()

    data = cv.fit_transform([c1,c2,c3])

    print(cv.get_feature_names())

    print(data.toarray())

    return None


if __name__ == '__main__':
    # Countvec()
    Hanzivec()