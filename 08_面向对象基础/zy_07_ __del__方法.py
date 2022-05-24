class Cat:
    def __init__(self,new_name):
        self.name = new_name

        print("%s 来了" %self.name)

    def __del__(self):

        print("%s 我去了" %self.name)


# Tom是一个全局变量，所有代码全部执行完毕，
# 才会删除全局变量，才会在最后执行__del__函数
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象，删除后会调用__del__方法
# del tom

print("-" * 50)

