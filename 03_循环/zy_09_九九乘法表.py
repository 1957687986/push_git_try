row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" %(col,row,col*row),end="\t")
        col += 1
    # 这行是在每行星星输出后增加换行
    print("")

    row += 1