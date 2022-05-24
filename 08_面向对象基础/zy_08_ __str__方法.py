class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)


    # 如果在开发过程中，希望使用print输出对象变量时，
    # 能够打印自定义的内容，就可以利用__str__这个内置方法
    def __str__(self):

        # 必须返回一个字符串
        return "我是小猫 [%s]" %self.name


# 使用 类名() 创建对象的时候，会自动调用初始化方法__init__
tom = Cat("Tom")

print(tom)
