import numpy as np
import random

# 随机种子 -- 第一次随机，之后每次一样
np.random.seed(10)
t1 = np.random.randint(10,20,(3,4))

print(t1)
