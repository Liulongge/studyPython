import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./08-多表联合.xlsx', sheet_name='Students')
scores = pd.read_excel('./08-多表联合.xlsx', sheet_name='Scores')

print(students)
print(scores)

# how='left': 无论数据存在与否，左边全部显示
# fillna(0): 数据找不到，填充0
# on='ID': 指定使用ID join
table = students.merge(scores, how='left', on='ID').fillna(0)
print(table)

 
