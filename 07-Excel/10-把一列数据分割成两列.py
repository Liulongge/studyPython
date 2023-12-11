import pandas as pd
employees = pd.read_excel('./10-把一列数据分割成两列.xlsx', index_col='ID')
# split(): 中如果不提供分割参数，默认为空格' '
# n=？: 保留切出来的前多少个字符，-1: 有多少个保留多少个；3: 仅保留前三个 
# split(expand=True) 是 Pandas 中的一个字符串函数，用于将包含多个子字符串的列拆分成多列。当 expand=True 时，返回一个数据框，每个拆分的子字符串都是一个新的列。
df = employees['Full Name'].str.split(expand=True)
print(employees)
# print(df)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]
print(employees)