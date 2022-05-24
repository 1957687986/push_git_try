class Dog(object):

    @staticmethod
    def run():
        print("小狗跑跑跑...")


# 通过类名.调用静态方法 - 不需要调用静态方法
Dog.run()