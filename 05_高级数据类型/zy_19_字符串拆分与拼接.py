poem_str = "登鹳雀楼\t  王之涣 \r  百日一山尽  黄河入海流 \n欲穷千里目\t \t更上一层楼"

print(poem_str)

# 1.拆分字符串
poem_list = poem_str.split()

print(poem_list)

# 2.合并字符串
result = " ".join(poem_list)

print(result)