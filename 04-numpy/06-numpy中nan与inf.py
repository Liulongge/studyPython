import numpy as np


# nan(NAN, Nan)：not a number表示不是一个数字
# 什么时候numpy中会出现nan？
# 读取本地文件，文件有缺失；当作了一个不适合的计算的时候（无穷大减去无穷大）
# 
# inf(-inf, inf)：infinity，inf表示正无穷大，-inf表示负无穷大
# 出现场景：数字除以0
# 
# 注意：
# 两个 nan不相等
# nan与任何数字计算都是nan
# 
#

print("========================== 统计非零元素个数")
t = np.arange(24).reshape(4, 6).astype(np.float64)
print("原始数组: \n", t) 
t[:, 0] = 0
print("首列赋值为0: \n", t)
print("统计数组中非零元素个数: \n", np.count_nonzero(t))

# 将某个元素赋值为nan
print("========================== 统计nan元素个数")
t = np.arange(1, 25).reshape(4, 6).astype(np.float64)
t[3, 4] = np.nan
print("t(3, 4)赋值为nan: \n", t)
# 利用 nan 不等于 nan统计数组中 nan 元素个数
print("统计数组中nan元素个数: \n", np.count_nonzero(t != t))
print("统计数组中nan元素个数: \n", np.count_nonzero(np.isnan(t)))

print("========================== nan与任何数字运算都是nan")
t = np.arange(1, 25).reshape(4, 6).astype(np.float64)
t[3, 4] = np.nan
print("原始数组: \n", t) 
print("nan参与运算: \n", np.sum(t))
print("nan参与运算: \n", np.sum(t, axis = 0))
print("nan参与运算: \n", np.sum(t, axis = 1))

print("========================== 将nan替换为0")
# 由于nan与任何数字进行计算都是nan
# 在数组中单纯的把nan设置为0合适吗？
# 不合适，如果替换之前均值大于0，替换之后均值肯定会变小。
# 一般采用均值或中值替换，或者直接删除有缺失值的一行
t[np.isnan(t)] = 0
print("nan参与运算: \n", np.sum(t))
print("nan参与运算: \n", np.sum(t, axis = 0))
print("nan参与运算: \n", np.sum(t, axis = 1))