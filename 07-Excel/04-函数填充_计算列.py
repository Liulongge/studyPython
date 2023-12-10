import pandas as pd

# def add2(x):
#     return x + 2

books = pd.read_excel('./04-函数填充_计算列.xlsx', index_col='ID')
# 函数填充，列 x 列
books['Price'] = books['ListPrice'] * books['Discount']
# 每本价格加2元
# books['Price'] = books['Price'].apply(add2)
# 使用lambda表达式
books['Price'] = books['Price'].apply(lambda x:x+2)
print(books)