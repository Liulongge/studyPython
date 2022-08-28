
# 1、为什么要学？ 
#     快捷、方便、科学计算基础库
# 2、什么是numpy？
#     一个在python中做科学计算的基础库，重在数值计算，也是大部分python科学计算库的基础，多用于大型多维数组上执行数值计算
# 

# 关键词：
# 生成数组：nm.array、
# 范围内取值：arange(beg, end, step)
# 保留x位小数：round(t)
# 查看/指定数据类型：dtype
# 修改数据类型：t.astype("dtype")
# 产看数组类型：type(t)

from random import random
import numpy as np
import random
# 使用numpy生成数组，得到ndarray数据类型
# np.array 生成数组
# type(t)  查看数组类型
# t.dtype  查看数据类型，int64、float32 ......
print("========================== 使用numpy生成数组，得到ndarray数据类型")
t1 = np.array([1, 2, 3,])
# [1 2 3]
print(t1)
# <class 'numpy.ndarray'>
print(type(t1))
# int64
print(t1.dtype)

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(0, 1, 0.2) # 和range类似，numpy独有。4 - 10，步长为2
print(t3)
print(type(t3))


print("========================== numpy中的数据类型, dtype")
t4 = np.array(range(1, 4), dtype = "float")
print(t4)
print("数据类型：", t4.dtype)

t5 = np.array([1, 0, 1, 1, 0], dtype = "bool")
print(t5)
print("数据类型：", t5.dtype)

print("========================== numpy中的数据类型(调整数据类型, astype)")
t6 = t5.astype("int8")
print(t6)
print("数据类型：", t6.dtype)

print("========================== numpy中的数据类型(numpy中的小数)")
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

print("========================== numpy中的数据类型(保留x位小数)")
t8 = np.round(t7, 2) # 取两位小数
print(t8)
print(t8.dtype)

# 创建全为0, 1的数组
print("========================== numpy中特殊数组创建")
t = np.ones((2, 3))
print("创建全为1的数组: \n", t)
t = np.zeros((2, 3))
print("创建全为0的数组: \n", t)
t = np.eye((5))
print("创建对角线为1的方阵: \n", t)

print("argmax取最大值位置: \n", np.argmax(t, axis=0))
t[t == 1] = -1
print("argmax取最大值位置: \n", np.argmin(t, axis=1))



print("========================== copy与view")
# copy与view
# a = b 完全不复制，a和b相互影响
# a = b[:] 视图的操作，一种切片，会创建显得对象a，但是a的数据完全由b保管，他们两个数据是完全一致的
# a = b.copy() 复制，a和b互不影响