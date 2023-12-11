import pandas as pd

students = pd.read_excel('./11-求和求平均.xlsx', index_col='ID')
temp = students[['Test_1', 'Test_2', 'Test_3']]
# axis轴: 从上到下，轴0；从左到右，轴1

row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
print(row_sum)
print(row_mean)
students['Total'] = row_sum
students['Average'] = row_mean
print('求取每一行平均值:\n',students)

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean(axis=0)
print('col_mean:\n',col_mean)
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)
print('求取每一列平均值:\n',students)