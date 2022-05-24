class A:
    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" %(self.num1,self.__num2))

    def test(self):
        print("父类公有方法 %d" %self.__num2)
        self.__test()


class B(A):

    def demo(self):

        # 1.在子类对象方法中，不可访问父类私有属性
        # print("访问父类私有属性 %d" %self.__num2)

        # 2.不可调用父类私有方法
        # self.__test()

        # 3.访问父类公有属性
        print("子类方法 %d" %self.num1)

        # 4.调用父类公有方法
        self.test()

# 创建子类对象

b = B()
# print(b)
b.demo()
# print(b.__num2)
# print(b.__test())
