import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font",family = "KaiTi")

file_path = "./directory.csv"

df = pd.read_csv(file_path)

# 使用matplotlib呈现出店铺总数前10
# 准备数据
"""
sort_values(by, axis=0, ascending=True, inplace=False, kind=‘quicksort’, na_position=‘last’)

①axis 如果axis=0，那么by=“列名”； 如果axis=1，那么by=“行名”；
②ascending: True则升序，可以是[True,False]，即第一字段升序，第二个降序
③inplace: 是否用排序后的数据框替换现有的数据框 ，True,或者False
④kind: 排序方法
⑤na_position : {‘first’, ‘last’}, default ‘last’，默认缺失值排在最后面
"""
data1 = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]

# print(data1)
# print(type(data1))
# pandas.Series( data, index, dtype, name, copy)
# index：数据索引标签，如果不指定，默认从 0 开始
_x = data1.index
_y = data1.values
print(_y)

# 画图
plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x)

plt.grid(alpha = 0.4)
plt.show()


