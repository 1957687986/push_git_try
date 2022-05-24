def sum_number(num):

    # 1. 出口
    if num == 1:
        return 1
    # 2.数字累加
    temp = sum_number(num - 1)

    return num + temp


result = sum_number(100)

print(result)