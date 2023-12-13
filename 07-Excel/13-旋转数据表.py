import pandas as pd

# 控制着可显示的列数，默认值为20
pd.options.display.max_columns = 999
videos = pd.read_excel('./13-旋转数据表.xlsx', index_col='Month')
print('旋转前原始数据:\n',videos)
table = videos.transpose()
print('旋转后数据:\n',table)