row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*",end="")
        col += 1
    # 这行是在每行星星输出后增加换行
    print("")

    row += 1