import pandas as pd

# Series类似于字典，但不是字典，因为他的索引可以是重复的。
# Series 是一种类似于一维数组的对象，由下面两部分组成：
# values：一组数据，ndarray 类型
# index：数据索引
# 顾名思义，我们在创建 Series 对象时，需要传递一组数据，该数据大多数时候是可迭代对象

# dictionary
d = {'x':100, 'y':200, 'z':300}
s1 = pd.Series(d)
print(s1)

L1 = [100, 200, 300]
L2 = ['x', 'y', 'z']
s1 = pd.Series(L1, index=L2)
print(s1)

s1 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s1)

# index: 行头
# name: 列头
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
df = pd.DataFrame({s1.name:s1, s2.name:s2, s3.name:s3})
print(df)
df = pd.DataFrame([s1, s2, s3])
print("加载方式不同，生成结构不同:\n",df)
