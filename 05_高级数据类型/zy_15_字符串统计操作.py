hello_str = "hello hello"

# 1.统计字符串长度
print(len(hello_str))

# 2.统计某个小字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("as"))

# 3.某个子字符串出现的位置
print(hello_str.index("llo"))
# 不存在会报错
# print(hello_str.index("as"))