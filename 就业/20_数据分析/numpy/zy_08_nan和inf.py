# nan 表示 读取本地文件为float时，数据出现缺失，就会出现nan
# inf表示正无穷  -inf表示负无穷

import numpy as np

t = np.arange(24).reshape((4,6)).astype('float')
print(t)
# 将数组中的一部分替换成nan
t[1,3:]=np.nan
print(t)

t1 = (np.nan == np.nan)
print(t1)

t2 = np.array([[ 0 , 1 , 2  ,3  ,4 , 5],
 [ 0 , 7 , 8  ,9 ,10, 11],
 [ 0 ,13 ,14 ,15, 16, 17],
 [ 0 ,19, 20, np.nan ,22 ,23]])
print(t2)

# t2[3,4] = np.nan
# print(t2)

print(np.count_nonzero(t2))

print(np.count_nonzero(t2!=t2))
