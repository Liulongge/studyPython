
import pandas as pd
import numpy as np

# pandas使用df.loc查询数据的方法
# 1、使用单个label值查询数据
# 2、使用值列表批量查询
# 3、使用数值区间进行范围查询
# 4、使用条件表达式查询
# 5、调用函数查询
print("========================== pandas查询数据")
df = pd.read_csv("./data/beijing_tianqi_2018.csv")
print("原始数据: \n", df.head())
df.set_index("ymd", inplace = True) # 设置索引值为年月日
print("设置索引值为年月日: \n", df.head())
print("索引值: \n", df.index)
# 替换掉温度的后缀
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype(np.int32)
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype(np.int32)
print("替换掉温度的后缀: \n", df.head())


print("1、使用label值查询数据: \n", df.loc["2018-01-03", ["bWendu", "yWendu"]])
print("2、使用列表批量查询数据: \n", df.loc[["2018-01-03", "2018-01-04", "2018-01-05"], ["bWendu","yWendu"]])
print("3、使用数值区间进行范围查询(行index): \n", df.loc["2018-01-03" : "2018-01-06", ["bWendu","yWendu"]])
print("3、使用数值区间进行范围查询(列index): \n", df.loc["2018-01-03" : "2018-01-06", "bWendu" : "fengxiang"])
print("4、使用条件表达式进行查询: \n", df.loc[df["yWendu"] < -10, :])  # 最低温度低于10度的列表
print("4、使用条件表达式进行查询(复杂条件查询): \n", df.loc[(df["bWendu"] <= 30) &
                    (df["yWendu"] >= 15) & (df["tianqi"] == "晴") & (df["aqiLevel"] == 1), :])
