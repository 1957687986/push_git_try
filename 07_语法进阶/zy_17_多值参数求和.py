def sum_numbers(*args):
    num = 0

    print(args)
    # 循环
    for n in args:
        num += n

    return num

result = sum_numbers(1,2,3,10,52)
print(result)