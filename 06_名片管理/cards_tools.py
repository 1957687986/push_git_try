# 记录所有的名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出操作")
    print("欢迎使用【名片管理系统】 V 1.0")
    print("*" * 50)

def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入邮箱：")
    # 2.使用用户输入信息建立一个名片字典
    card_dict = {"name" : name_str,
                 "phone" : phone_str,
                 "qq" : qq_str,
                 "email" : email_str}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户添加成功
    print("添加 %s 的名片成功！" %name_str)
def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 没有记录提示
    if len(card_list) == 0 :
        print("没有记录")
        # return 可以返回一个函数的执行结果
        # 下方代码不会被执行
        return
    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t\t\t")

    print("")
    # 打印分割线
    print("-" * 50)
    for card_dict in card_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" %(card_dict["name"],
              card_dict["phone"],card_dict["qq"],card_dict["email"]))

def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入姓名：")

    # 2.遍历
    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("找到了")
            print("姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱")
            print("-" * 50)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" % (card_dict["name"],
                                                        card_dict["phone"], card_dict["qq"], card_dict["email"]))
            # 对名片执行修改和删除操作
            deal_card(card_dict)
            break
    else:
        print("没找到%s" %find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    action_str = input("亲选择需要执行的操作 [1] 修改 "
                       "[2] 删除 [0] 返回上级菜单:")
    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"],"姓名[回车不修改]：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话[回车不修改]：")
        find_dict["qq"] = input_card_info( find_dict["qq"],"QQ[回车不修改]：")
        find_dict["email"] = input_card_info(find_dict["email"],"邮箱[回车不修改]：")
        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("删除名片成功")

def input_card_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示信息
    :return: 如果输入内容，返回内容，否则返回原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，输入内容返回结果
    if len(result_str) > 0:
        return result_str

    # 3. 不输入返回字典中原有的值
    else:
        return dict_value