class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    # 类属性！！！
    count = 0

    def __init__(self,name):

        # 对象属性！！！
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# print(Tool.count)

# 此count为赋值语句，在该对象中没有该属性，
# 会在对象中添加一个count属性
tool1.count = 99

print("工具对象总数 %d" %tool1.count)
print("Tool==>工具对象总数 %d" %Tool.count)
