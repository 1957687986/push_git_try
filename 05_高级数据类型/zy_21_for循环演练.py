for num in [1,2,3]:
    if num == 2:
        break
    print(num)

else:
    # 如果for循环由break退出则else不会执行
    print("会执行吗？")
print("循环结束")