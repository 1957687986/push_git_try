def demo(num, num_list):
    print("函数开始")

    num += num
    # 列表变量使用 += 不会做相加再赋值操作
    # 本质上是调用列表中的extend方法 方法会改值！！！ 赋值不会改值！！！
    num_list += num_list
    print(num)
    print(num_list)

    print("参数完成")

gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)