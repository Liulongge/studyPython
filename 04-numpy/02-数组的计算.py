

from cmath import nan
import numpy as np

# nan：非常小
# inf：无穷大
# 一维数组
print("========================== 一维数组")
t1 = np.arange(12)
print(t1.shape)
print(t1)
# 二维数组
print("========================== 二维数组")
t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2.shape)
print(t2)
# 三维数组
print("========================== 三维数组")
t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t3.shape)
print(t3)

print("========================== 修改数组维度reshape")
# reshape不会改变原有数组形状，有返回值的操作，一般不会改变原有形状
t4 = np.arange(12)
t5 = t4.reshape((3, 4))
print(t5.shape)
print(t5)
t55 = t4.reshape((12,))
print(t55.shape)
print("转换为1维: ", t55)

print("========================== 修改数组维度flatten")
# 数组按行进行展开成一维
t6 = t5.flatten()
print(t5)
print(t6.shape)
print("flatten: ", t6)


# 加法运算
print("========================== 加/减运算")
t7 = np.arange(0, 24).reshape(4, 6)
t8 = np.arange(100, 124).reshape(4, 6)
t9 = np.arange(0, 4).reshape(4, 1)
print("t7: \n", t7)
print("t8: \n", t8)
print("t9: \n", t9)
print("t7 + t8: \n", t7 + t8)
print("t7 + 2: \n", t7 + 2)
print("t8 - t7: \n", t8 - t7)
print("t7 - 2: \n", t7 - 2)
print("t7 - t9: \n", t7 - t9) # t7 的每一列均减去 t9

