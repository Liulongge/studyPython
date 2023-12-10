import pandas as pd

data = pd.read_excel('./output.xlsx')
# 遇到比较脏的header时候，将指定行作为header
# data = pd.read_excel('./output.xlsx', header=1)
print('数据:\n', data)
# 查看有多少行，多少列
print('查看有多少行，多少列:\n', data.shape)
# 查看每列的标题
print('查看每列的标题:\n', data.columns)
# 取数据的前n行数据，默认5行
print('读取数据的前n行数据\n', data.head(2))
# 取数据的后n行数据，默认5行
print('读取数据的后n行数据\n', data.tail(2))

print("================== 没有header ==================")
# Excel没有header的情况下，设置为None
data = pd.read_excel('./no_header.xlsx', header=None)
print('没有header:\n', data)
# 人为设置header
data.columns = ['ID', 'Name']
data = data.set_index('ID')
print('人为设置header:\n', data)