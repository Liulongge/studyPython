import pandas as pd
import numpy as np

# 1、汇总类统计
# 2、唯一性去重和按值计算
# 3、相关系数和协方差

print("========================== 数据统计函数")
df = pd.read_csv("./data/beijing_tianqi_2018.csv")
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype(np.int32)
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype(np.int32)
print("原始数据: \n", df.head(3)) # 查看前三行

print("========================== 1、汇总类统计")
# 一下提取所有数字统计结果
print("汇总类统计: \n", df.describe())
print("查看单个Series数据: \n", df["bWendu"].mean())
print("最高温度: \n", df["bWendu"].max())
print("最低温度: \n", df["yWendu"].min())


print("========================== 2、唯一性去重和按值计算")
print("========================== 2、唯一性去重")
# 一般不用于值列，而是枚举，分类列
print("唯一性去重, 风向: \n", df["fengxiang"].unique()) # 
print("唯一性去重, 天气: \n", df["tianqi"].unique()) # 一般不用于值列，而是枚举，分类列
print("唯一性去重, 风力: \n", df["fengli"].unique()) # 一般不用于值列，而是枚举，分类列


print("========================== 2、按值计数")
print("按值计数, 风向: \n", df["fengxiang"].value_counts())
print("按值计数, 天气: \n", df["tianqi"].value_counts())
print("按值计数, 风力: \n", df["fengli"].value_counts())


print("========================== 3、相关系数和协方差")
# 用途：
# 1、两支股票是不是同时涨同时跌？程度多大？正相关还是负相关？
# 2、产品销量的波动，跟哪些因素正相关、负相关、程度多大？
# 协方差：衡量同向反向程度，如果协方差为正，说明x, y同向变化，协方差越大说明同向程度越高。
#        如果协方差为负数，说明x，y反方向运动，协方差越小，方向程度越高
# 相关系数：衡量相似程度，当相关系数为1时，两个变量变化时的正向相似度最大，当相关系数为-1时，变量反向相似度越大
print("协方差矩阵: \n", df.cov().head())
print("相关系数矩阵: \n", df.corr().head())

print("相关系数矩阵，空气质量与最高温度: \n", df["aqi"].corr(df["bWendu"]))
print("相关系数矩阵，空气质量与最低温度: \n", df["aqi"].corr(df["yWendu"]))

print("相关系数矩阵，空气质量与温差: \n", df["aqi"].corr(df["bWendu"] - df["yWendu"]))
