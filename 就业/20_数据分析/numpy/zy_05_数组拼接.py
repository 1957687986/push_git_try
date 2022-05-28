import numpy as np

t1 = np.arange(12).reshape((2,6))
t2 = np.arange(12,24).reshape((2,6))

print(t1)
print("*" * 50)
print(t2)
print("*" * 50)

t3 = np.vstack((t1,t2))
print(t3)
print("*" * 50)

t4 = np.hstack((t1,t2))
print(t4)
print("*" * 50)

# 交换行列的顺序
t5 = np.arange(12,24).reshape(3,4)
t5[[1,2],:] = t5[[2,1],:]
print(t5)
print("*" * 50)
