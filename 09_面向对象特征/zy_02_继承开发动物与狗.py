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
    # def eat(self):
    #
    #     print("吃---")
    #
    # def drink(self):
    #
    #     print("喝---")
    #
    # def run(self):
    #
    #     print("跑---")
    #
    # def sleep(self):
    #
    #     print("睡---")

    def bark(self):

        print("旺旺叫")

wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()