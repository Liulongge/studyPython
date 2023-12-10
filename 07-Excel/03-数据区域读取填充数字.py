import pandas as pd
from datetime import date, timedelta

# skiprows: 跳过前面几行数据
# usecols: 使用A->B列数据
books = pd.read_excel('./03-数据区域读取填充数字.xlsx', skiprows=3, usecols='C:F', index_col=None)
print(books)

start = date(2018, 1, 1)
for i in books.index:
    books['ID'].at[i] = str(i + 1)
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    books['Date'].at[i] = start + timedelta(days=i)

books.set_index('ID', inplace=True)
print(books)
books.to_excel('./03-数据区域读取填充数字2.xlsx')