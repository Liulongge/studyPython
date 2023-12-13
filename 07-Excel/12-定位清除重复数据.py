import pandas as pd

students = pd.read_excel('./12-定位清除重复数据.xlsx')
print(students)
# drop_duplicates: pandas出重函数
# keep='first'/'last': 出现重复数据时，保留前面还是后面
# students.drop_duplicates(subset='Name', inplace=True, keep='first')
# print(students)

dupe = students.duplicated(subset='Name')
print('检查是否是重复数据:\n',dupe)
print('检查是否存在重复数据:\n',dupe.any())
dupe = dupe[dupe == True]
print('哪些数据是重复的:\n',dupe.index)
print('重复数据:\n',students.iloc[dupe.index])
