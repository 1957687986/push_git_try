has_ticket = True

knife_length = 10

if has_ticket :
    print("车票通过，准备安检")
    if knife_length > 20:
        print("刀太长")
    else:
        print("刀合适")
else:
    print("请先买票")