from sklearn.preprocessing import StandardScaler

# 转换器
s = StandardScaler()

data_s = s.fit_transform([[1, 2, 3], [4, 5, 6]])

print(data_s)

ss = StandardScaler()

data_ss = ss.fit([[1,2,3],[4,5,6]])

print(data_ss)

print(ss.transform([[1,2,3],[4,5,6]]))

# 估计器  --  实现算法的API