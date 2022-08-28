from typing import ValuesView
import numpy as np


# 创建d0-dn维度均匀分布的随机数数组，浮点数，范围0~1
a = np.random.rand(2,3)
print("rand 随机数组: \n", a)

# 返回一个符合标准正态分布的数组
a = np.random.randn(2,3)
print("randn 随机数组: \n", a)

# 返回一定范围的一维或者多维整数
# numpy.random.randint(low, high = None, size = None, dtype=’l’)
# 返回随机整数，范围区间为[low,high），包含low，不包含high
# size为数组维度，元组形式，如（2,3）#2行3列
# high没有填写时，默认生成随机数的范围是[0，low)
# dtype指定数据类型，默认int
a = np.random.randint(low = 6, high = 10, size=(2, 3), dtype = 'int')
print("randint 随机数组: \n", a)

# np.random.uniform(low=0.0, high=1.0, size=None)，生成符合指定均匀分布的数组
a = np.random.uniform(-1, 1, 10)#指定均匀分布
print("uniform 随机数组: \n", a)

# np.random.normal(loc=0.0, scale=1.0, size=None),生成符合指定分布的正态分布
a = np.random.normal(loc = 4, scale = 6,size = (2,3))
print("normal 随机数组: \n", a)

# numpy.random.seed(n) 其中n为任意指定
# 当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
np.random.seed(0)
a = np.random.rand(4)  
print("seed 随机数组: \n", a)

