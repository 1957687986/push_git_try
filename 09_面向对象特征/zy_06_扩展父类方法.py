class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


class xiaotianquan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):

        # 针对子类特有需求，编写代码
        print("叫的好")

        # 使用super（）调用原本在父类中封装的方法
        super().bark()

        # 增加其他子类的代码
        print("%$#^$&^")



xtq = xiaotianquan()

xtq.bark()
xtq.run()