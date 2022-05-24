def sum_number(num):

    print(num)
    # 递归出口
    if num == 1:
        return

    sum_number(num - 1)

sum_number(3)
