name_list = ["zhangsan","lisi","wangwu","wangxiaoer"]

"""
顺序地从列表中依次获取数据，每次循环过程中都会保存在
my_name 这个变量中，在循环体中都可以访问到当前这一次获取到的数据
"""

for my_name in name_list:
    print("我的名字叫 %s " % my_name)