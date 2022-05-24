info_tuple = ("zhangsan",18,1.75)

# 取值和取索引
print(info_tuple[0])

# 取索引：已经知道数据的内容，希望知道数据在元组中的索引，即位置
print(info_tuple.index("zhangsan"))

# 统计计数
print(info_tuple.count("zhangsan"))

# 统计元组长度
print(len(info_tuple))