students = [
    {"name" : "阿如"},
    {"name" : "小妹"}
]

find_name = "阿如"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" %find_name)
        # 如果找到应该直接退出循环，不再执行后续遍历
        break

else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到一个统一的提示
    print("没找到 %s" %find_name)


print("循环结束")