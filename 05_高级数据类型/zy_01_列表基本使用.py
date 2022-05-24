name_list = ["zhangyuan","lisi","wangwu"]

# 取值、取索引
print(name_list[0])

print(name_list.index("lisi"))
print(name_list)

# 修改
name_list[1] = "李四"
print(name_list)

# 增加
# append在末尾增加数据
name_list.append("王小二")
# insert在列表指定位置上增加数据
name_list.insert(1,"小美眉")
# extend可以把其他的列表增加到一个列表后
temp_list = ["孙悟空","猪二哥","沙师弟"]
name_list.extend(temp_list)
print(name_list)

# 删除
# remove可以从列表中删除指定数据
name_list.remove("wangwu")
# pop默认把列表中最后一个元素移除列表
name_list.pop()
# pop可以删除指定位置的元素
name_list.pop(3)
# clear清空整个列表
name_list.clear()

print(name_list)
