
# https://www.bilibili.com/video/BV1UJ411A7Fs?p=3&spm_id_from=pageDriver&vd_source=6b48595092f05a0fc1d129f83872951f
import pandas as pd

print("========================== 读取csv文件")
t = pd.read_csv("./data/ratings.csv")
print("读取数据前几行数据: \n", t.head())
print("查看数据形状，返回行列: \n", t.shape)
print("查看数据columns列名列表: \n", t.columns)
print("查看数据index索引列表: \n", t.index)
print("查看每列数据类型: \n", t.dtypes)

print("========================== 读取txt文件")
t = pd.read_csv("./data/access_pvuv.txt", sep = "\t", header = None, names = ["pdata", "pv", "uv"])
print("读取数据前几行数据: \n", t.head())
print("查看数据形状，返回行列: \n", t.shape)
print("查看数据columns列名列表: \n", t.columns)
print("查看数据index索引列表: \n", t.index)
print("查看每列数据类型: \n", t.dtypes)

print("========================== 读取excel文件")
t = pd.read_excel("./data/access_pvuv.xlsx")
print("读取数据前几行数据: \n", t.head())
print("查看数据形状，返回行列: \n", t.shape)
print("查看数据columns列名列表: \n", t.columns)
print("查看数据index索引列表: \n", t.index)
print("查看每列数据类型: \n", t.dtypes)
