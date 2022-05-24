hello_str = "hello hello"

# 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 判断是否以指定字符串结束
print(hello_str.endswith("hello"))

# 查找指定字符串
# index同样可以查找指定字符串在大字符串中的索引,
# index指定的字符串不存在，代码报错
# find指定的字符串不存在，返回-1
print(hello_str.find("llo"))
print(hello_str.find("asd"))

# 替换字符串
# replace 方法执行后会返回新的字符串（所有的hello全部替换为world）
# 注意不会改变原有字符串的值
print(hello_str.replace("hello","world"))
print(hello_str)
