# 在开发中是把多个字典放在一个列表中，在进行遍历
card_list = [
    {"name": "张三",
     "qq": "123456",
     "phone": "1885"},
    {"name": "李四",
     "qq": "123476",
     "phone": "1585"}
]

for card_info in card_list:
    print(card_info)