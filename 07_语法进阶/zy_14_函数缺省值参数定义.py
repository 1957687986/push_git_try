def print_info(name , gender = True):

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" %(name,gender_text))

# 假设男生居多
# 指定缺省参数的默认值，应该是用最常见的值作为默认值
print_info("小明")
print_info("老王")
print_info("小妹",False)