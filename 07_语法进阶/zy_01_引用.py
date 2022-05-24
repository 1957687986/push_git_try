def test(num):
    print("在函数内部%d对应的内存地址是%d" %(num ,id(num)))
    num = 11

    result = "hello"

    print("函数要保存的内存地址是：%d" %id(result))

    return  result

# 1. 定义一个数字的变量
a = 10

print("a变量保存数据的地址是：%d" %id(a))
print(a)

# 2. 调用test函数,本质上是传递的是实参保存数据的引用，而不是实参保存的数据

# 有返回值但不接受，不会报错，但是接收不到数据
r = test(a)
print("%s 的内存地址是 %d" %(r,id(r)))
print(a)