import pandas as pd
import numpy as np

file_path = "./directory.csv"

df = pd.read_csv(file_path)

grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()

# 索引的方法与属性
print(grouped1.index)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=["a","b","c"],columns=list("wxyz"))
print(df1)

print(df1.reindex(["a","f"]))

# 以某一列作为索引
print(df1.set_index("w",drop=False))
print(df1)


