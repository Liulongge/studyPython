

# 轴(axis)，在numpy中可以理解为方向，使用0, 1, 2, 3 .....数字表示，对于一个一维数组，只有一个0轴，
# 对于二维数组，有0轴和1轴，对于3维数组，有1, 2, 3轴


import numpy as np
print("========================== 读取本地数据")
us_file_path = "./data/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./data/youtube_video_data/GB_video_data_numbers.csv"


# np.loadtxt（frame, dtype, delimiter, skiprows, usecols, unpack）
# 参数解释：
# frame：传进去一个路径
# dtype：保存后的数据类型，默认是float eg：dtype=int
# delimiter：分隔字符, 默认是空格eg：delimite = None
# skiprows：跳过前几行，一般跳过第一行 eg：skipeows = 0
# usecols：读取指定的列，索引元组类型
# unpacks： 如果True, 就让转置数据反转过来，通俗来讲其实就是行变成列，列变成行。默认是False

t1 = np.loadtxt(us_file_path, delimiter=",",dtype="int")
t2 = np.loadtxt(uk_file_path, delimiter=",",dtype="int")
print(t1)
print(t2)


# numpy转置
print("========================== numpy转置")
t = np.arange(24).reshape(4,6)
t2 = t.transpose()
t3 = t.T
t4 = t.swapaxes(1,0)
print("转置前：\n", t)
print("转置后：\n", t3)


# numpy索引和切片
# 逗号前指明行，逗号后指明列
print("========================== 取列")
t = np.arange(36).reshape(6,6)
print("原始数据: \n", t)
print("取某一行: \n", t[2])   # 取出第3行
# print(t2[2, :])
print("取连续多行: \n", t[2:])   # 取连续多行，取出第3行及之后全部
# print(t2[2:, :]) 
# 取不连续多行
print("取不连续多行: \n", t[[1, 3, 5]])
# print(t2[[1, 3, 5], :])


# 取列
print("========================== 取列")
t = np.arange(36).reshape(6,6)
print("原始数据: \n", t)
print("取某一列: \n", t[:, 2]) # 取一行
print("取连续多列: \n", t[:, 2:]) # 取连续多行
print("取不连续多列: \n", t[:, [0, 2, 5]]) # 取不连续多行

# 取多行和多列
print("========================== 取多行和多列")
t = np.arange(36).reshape(6,6)
print("原始数据: \n", t)
# 取第三行第四列的值
print("3行4列的数据: \n", t[3, 4])
print("3-5行, 2-4列的数据: \n", t[3:5, 2:4])
print("多个不相邻的点, (0, 0), (2, 3), (3, 4): \n", t[[0, 2, 3], [0, 3, 4]])
