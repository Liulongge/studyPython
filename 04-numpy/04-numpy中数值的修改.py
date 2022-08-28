# 总结
# np.where( , , ), numpy中的三目运算符
# np.clip(t, min, max), 用于限制数组上线界
# np.vstack((t1, t2)), 竖直拼接
# np.hstack((t1, t2)), 水平拼接
# 行列交换


import numpy as np

print("========================== numpy中数值的修改")
# 直接索引出元素，修改值即可
t = np.arange(36).reshape(6,6)
print("原始数据: \n", t)
t[3, 4] = 9999
print("修改(3, 4)的数据: \n", t)

t[:, 3] = 3333
print("修改3列的数据: \n", t)

# 小于10的数据全部赋值为0
t[t < 10] = 0
print("小于10的数据赋值为0: \n", t)


print("========================== numpy中三元运算符")
# where
t = np.arange(36).reshape(6,6)
print("原始数据: \n", t)
t = np.where(t < 10, 0, 10)
print("小于10等于0, 大于10等于10: \n", t)

print("========================== numpy中clip(裁剪)")
# clip（）截断，限制数组的上下界
# np.clip(a, min, max, out = None)
t = np.arange(36).reshape(6,6)
print("原始数据: \n", t)
t = np.clip(t, 10, 30)
print("clip 小于10等于10, 大于30等于30: \n", t)


print("========================== numpy中数组的拼接")
# 水平拼接 np.hstack((t1, t2))
# 竖直拼接 np.vstack((t1, t2))
t1 = np.arange(0, 12).reshape(2,6)
t2 = np.arange(12, 24).reshape(2,6)
print("原始数据t1: \n", t1)
print("原始数据t2: \n", t2)
t3 = np.vstack((t1, t2))
t4 = np.hstack((t1, t2))
print("竖直拼接: \n", t3)
print("水平拼接: \n", t4)

print("========================== numpy中数组的行列交换")
t1 = np.arange(36).reshape(6, 6)
print("原始数据t1: \n", t1)
t1[[1, 2], :] = t1[[2, 1], :]
print("1, 2行交换: \n", t1)
t1 = np.arange(36).reshape(6, 6)
t1[:, [1, 2]] = t1[:, [2, 1]]
print("1, 2列交换: \n", t1)

