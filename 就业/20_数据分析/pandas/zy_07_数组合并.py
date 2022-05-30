import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list("abcd"))
df2 = pd.DataFrame(np.zeros((3,3)),index=["A","B","C"],columns=list("xyz"))

# join按照行索引来合并
df3 = df1.join(df2)
df4 = df2.join(df1)

print(df3)
print(df4)

df5 = pd.DataFrame(np.array(9).reshape((3,3)),columns=list("fax"))

# merge按照列索引来合并
df1.merge(df5,on="a",how="")