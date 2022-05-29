import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("wxyz"))

print(t)

d1 = {"name":["xiaoming","xiaogang"],
      "age":[30,32],
      "tel":[10086,10010]}

t1 = pd.DataFrame(d1)

print(t1)

d2 = [{"name":"xiaoming",
       "age":30,
       "tel":10086},
      {"name":"xiaogang",
       "age":32,
       "tel":10010},
      {
          "name":"xiaowang",
          "tel":10050
      }]

t2 = pd.DataFrame(d2)

print(t2)

print(t2.index)
print(t2.columns)
print(t2.values)
print(t2.shape)
print(t2.dtypes)
# 数据维度
print(t2.ndim)


