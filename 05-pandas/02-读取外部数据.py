
import pandas as pd
import numpy as np

t = pd.read_csv("../04-numpy/data/youtube_video_data/GB_video_data_numbers.csv")
print(t)

# DataFrame有行索引又有列索引
# 行索引：表明不同行，横向索引，叫index, 0轴，axis = 0
# 列索引：表明不同列，纵向索引，叫colmns, 1轴，axis = 1
t = pd.DataFrame(np.arange(36).reshape(6, 6), index = list("abcdef"), columns=list("uvwxyz"))
print("创建DataFrame: \n", t)

print("========================== 由字典创建DataFrame 1")
d = {"name" : ["xiaoming", "xiaohong"], "age" : [20, 32], "tel" : [10086, 10010]}
t = pd.DataFrame(d)
print("由字典创建DataFrame 1: \n", t)

print("========================== 由字典创建DataFrame 2")
d = [
{"name" : "xiaoming", "age" : 20, "tel" : 10086}, 
{"name" : "xiaohong", "age" : 32, "tel" : 10010},
{"name" : "xiaozhang", "age" : 32}]
t = pd.DataFrame(d)
print("由字典创建DataFrame 2: \n", t)