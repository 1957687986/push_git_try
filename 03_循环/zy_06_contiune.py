i = 0
while i < 10:
    # i == 3 跳过循环
    if i == 3:
        # 再循环中使用continue这个关键字
        # 需要确认计数是否修改
        # 否则会出现死循环
        i += 1
        continue
    print(i)
    i += 1
print("over")