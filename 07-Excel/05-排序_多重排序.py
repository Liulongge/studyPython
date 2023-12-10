import pandas as pd

products = pd.read_excel('./05-排序_多重排序.xlsx', index_col='ID')
# inplace: 在当前frame进行修改
# ascending: 排序方式，默认从小到大
products.sort_values(by='Price', inplace=True, ascending=False)
print("排序:\n",products)

# 多重排序
# 将'by' 传递一个list
products.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=[True, False])
print("多重排序:\n",products)

