
import pandas as pd
import numpy as np

# 在进行数据分析时，经常需要按照一定条件创建新的据列，然后进行进一步分析
# 1、直接赋值
# 2、df.apply方法
# 3、df.assign方法
# 4、按条件选择分组分别赋值

print("========================== pandas新增数据列")
df = pd.read_csv("./data/beijing_tianqi_2018.csv")
print("原始数据: \n", df.head())

# 1、直接赋值的方法
# 清理温度列，变为数字类型
print("========================== 直接赋值")
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype(np.int32)
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype(np.int32)
print("直接赋值: \n", df.head())
# 计算温差
df.loc[:, "wencha"] = df["bWendu"] - df["yWendu"]
print("计算温差: \n", df.head())

print("========================== df.apply")
# 添加一列温度类型
# 如果温度高于33属于高温
# 低于 -10是低温
# 否则是常温
def get_wendu_type(x) :
    if x["bWendu"] > 33 :
        return "高温"
    if x["yWendu"] < -10 :
        return "低温"
    return "常温"

df.loc[:, "wendu_type"] = df.apply(get_wendu_type, axis = 1)
print("添加温度类别: \n", df.head())
print("查看温度类别计数: \n", df["wendu_type"].value_counts())

print("========================== df.assign")
# 将温度从摄氏度变为华氏度
# 可以同时添加多个新列
# 返回的是一个新的对象，不会改变原来值
print("添加温度类别: \n", 
    df.assign(
        yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,
        bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32,
    ).head()
)

print("========================== 按条件选择分组分别赋值")
# 按条件先选择数据，然后对这部分数据赋值新列
# 实例：高低温差大于10度，认为温差大
df["wencha_type"] = ""
df.loc[df["bWendu"] - df["yWendu"] > 10, "wencha_type"] = "温差大"
df.loc[df["bWendu"] - df["yWendu"] < 10, "wencha_type"] = "温差正常"
print("添加温度类别: \n", df.head())