
import numpy as np

# 默认返回多维数组全部统计结果，如果指定axis则返回当前轴上的结果
# 求和函数：sum
# 求均值函数：mean
# 求中值(中位数)函数：median
# 求最大值函数：max
# 求最小值函数：min
# 求极值函数：ptp，最大值与最小值的差
# 求标准差函数：std

print("========================== 常用统计函数")
t = np.arange(36).reshape(6, 6)
print("原始数组: \n", t) 
print("求和: \n", np.sum(t)) 
print("求均值: \n", np.mean(t)) 
print("求中值: \n", np.median(t)) 
print("求最大值: \n", np.max(t))
print("求最小值: \n", np.min(t))
print("求极值: \n", np.ptp(t))
print("求标准差: \n", np.std(t))
 
print("========================== 把nan替换为均值")
t = np.arange(36).reshape(6, 6).astype(np.float64)
print("原始数组: \n", t)
t[[2, 3], :] = np.nan
print("填充个nan后的数组: \n", t)
for i in range(t.shape[1]) : # 遍历每一列
    temp_col = t[:, i] # 当前的一列
    nan_nums = np.count_nonzero(temp_col != temp_col)
    if nan_nums != 0 : #当前这一列中有nan
        temp_not_nan_col = temp_col[temp_col == temp_col] # 当前一列不为nan的一列
        temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean() # 选中当前为nan的位置，把值赋值为不为nan的均值

print("填充个nan后的数组: \n", t)       





