# 把全局变量放到所有函数上方
num = 10


def demo():
    print("%d" %num)
    print("%s" %title)
    # print("%s" %name)

title = "ashbd"

demo()


# 不可，还没有执行到这一步
# name = "xiaominh"