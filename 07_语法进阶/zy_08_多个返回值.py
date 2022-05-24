def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组—可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果返回的是元组（）是可以省略的
    return temp,wetness

result = measure()
print(result)

# 需要单独处理温度或湿度 - 不方便
print(result[0])
print(result[1])

# 如果函数返回类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接受函数的返回值
# 元素个数注意保持一致
gl_temp , gl_wetness = measure()

print(gl_temp)
print(gl_wetness)