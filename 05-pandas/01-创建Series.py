
# numpy能够处理数值型数据，很多时候除了数值型数据以外，还有字符串、时间序列等
# numpy能够处理数值型数据，pandas能够处理数值型数据以外，还能处理其他类型数据

# pandas常用数据类型：
# Series: 一维带标签数组
# dataframe: 二维series容器

import pandas as pd

print("========================== 创建Series")
t = pd.Series([1, 2, 31, 12, 3, 4])
print(t)

t = pd.Series([1, 2, 31, 12, 3, 4], index=list("abcdef"))
print(t)


# 由字典创建Seres
print("========================== 创建Series(由字典创建Series)")
temp_dict = {"name": "xiaoming", "age": 16, "tel": 10086}
t = pd.Series(temp_dict)
print(t)

print("========================== 索引")
print("通过索引取值: \n", t["name"])
print("通过位置取值: \n", t[0])
print("连续取值: \n", t[:2])
print("不连续取值: \n", t[[1, 2]])
print("通过索引取多行数据: \n", t[["name", "tel"]])