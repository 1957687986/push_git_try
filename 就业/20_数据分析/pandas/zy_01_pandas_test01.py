import pandas as pd

# Series 一维，带标签数组
t1 = pd.Series([1,2,31,12,2,4])

t2 = pd.Series([1,3,445,6,5,2],index=list("abcdef"))

print(t1)
print(t2)

temp_dict = {"name":"xiaohong",
             "age":30,
             "tel":10086}

t3 = pd.Series(temp_dict)
print(t3)
print(t3["age"])
print(t3[[1,2]])
print(t3.index)

for i in t3.index:
    print(i)

print(len(t3.index))

print(t3.values)
