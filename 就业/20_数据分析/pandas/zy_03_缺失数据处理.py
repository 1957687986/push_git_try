from pymongo import MongoClient
import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("wxyz"))

t.iloc[1:,:2] = np.nan

print(pd.isnull(t))

# 选择t中 w这一列不为nan的那一行
# pd.notnull(t["w"])选中w这一列中不为nan的值 传入t再去选择那一行
print(t[pd.notnull(t["w"])])

# 删除  how选中全部为nan的那一行进行删除 -- 但是默认是只要有nan就进行删除
print(t.dropna(axis=0,how="all"))

# inplace 为原地修改，即直接修改t的值
# t.dropna(axis=0,how="any",inplace=True)

# 填充nan
print(t.fillna(t.mean()))

# 如果要修改t的值需要重新把t["w"].fillna(t["w"].mean())赋值给t["w"]
print(t["w"].fillna(t["w"].mean()))

print(t)
