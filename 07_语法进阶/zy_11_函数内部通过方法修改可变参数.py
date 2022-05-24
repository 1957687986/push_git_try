def demo(num_list):
    print("函数内部代码")

    # 使用了方法对参数进行修改（可变参数）
    num_list.append(9)

    print(num_list)
    print("函数执行完后")

gl_list = [1,2,3]
demo(gl_list)
print(gl_list)