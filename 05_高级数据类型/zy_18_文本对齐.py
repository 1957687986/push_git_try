poem = ["登鹳雀楼",
        "王之涣",
        "百日一山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

# 左对齐 ljust 右对齐 rjust

for poem_str in poem:
    print("|%s|" %poem_str.center(10," "))

print(poem)