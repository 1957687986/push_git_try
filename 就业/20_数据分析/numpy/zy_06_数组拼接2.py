import numpy as np

# 加载国家数组
us_data_path = ""
uk_data_path = ""

us_data = np.loadtxt(us_data_path,delimiter=",",dtype=int)
uk_data = np.loadtxt(uk_data_path,delimiter=",",dtype=int)

# 添加国家信息
# 构造全为0的数组
zero_data = np.zeros((us_data.shape[0],1)).astype(int)
one_data = np.ones((uk_data.shape[0],1)).astype(int)

# 分别添加一列全为0,1的数组
us_data = np.hstack((us_data,zero_data))
uk_data = np.hstack((uk_data,one_data))

# 拼接数组
final_data = np.vstack((us_data,uk_data))
print(final_data)
