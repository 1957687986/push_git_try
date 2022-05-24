xiaoming_dict = {"name": "小明"}

# 1.取值
print(xiaoming_dict["name"])

# 2.增加/修改
# key不存在会新增键值对
xiaoming_dict["age"] = 18
# key存在会修改值
xiaoming_dict["name"] = "小小明"
print(xiaoming_dict)

# 3.删除
xiaoming_dict.pop("name")

print(xiaoming_dict)