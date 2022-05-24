# 为外界提供全局变量、函数、类，注意直接执行的代码不是想外界提供的工具；

def say_hello():
    print("你好你好，我是say_hello")

# 如果直接执行模块，结果为：__main__
# 由其他模块导入时不执行
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够被执行的代码不需要被执行！
    print("小明开发的模块")
    say_hello()