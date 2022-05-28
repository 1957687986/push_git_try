import numpy as np

t1 = np.arange(12).reshape((3,4)).astype("float")

t1[1,2:] = np.nan
"""
[[ 0.  1.  2.  3.]
 [ 4.  5. nan nan]
 [ 8.  9. 10. 11.]]      ==>t1
"""
print(t1)

print(t1.shape[1])
# print(t1)

def fill_ndarray(t1):
    for i in range(t1.shape[1]): # 遍历每列
        temp_col = t1[:,i]  # 当前一列
        print(np.count_nonzero(temp_col!=temp_col)) # 判断是否有nan -- 结果为 0011
        nan_num = np.count_nonzero(temp_col!=temp_col)
        if nan_num != 0:  # 说明有nan
            print(temp_col == temp_col)  # 判断数组中的数字是否为nan -- 结果 [ True False  True]
            print(temp_col[temp_col == temp_col])  # 找出数字 -- 结果为 [ 2. 10.]
            temp_npt_nan_col = temp_col[temp_col == temp_col] #当前一列不为nan的array
            # 选中当前为nan的地方将值赋为 不为均值
            temp_col[np.isnan(temp_col)] = temp_npt_nan_col.mean()
    return t1

if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype("float")

    t1[1, 2:] = np.nan
    print(t1)
    print("*" * 20)
    t1 = fill_ndarray(t1)
    print(t1)
    