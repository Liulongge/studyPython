
# 默认索引
# df = df.set_index('ID')
#    ID    Name
# 0   1     Tim
# 1   2  Victor

# 修改索引为'ID'
# ID     Name       
# 1      Tim
# 2   Victor
# 3     Nick

import pandas as pd
df = pd.DataFrame({'ID':[1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})
df = df.set_index('ID')
# 将'ID'设置为第一列索引(否则第一列默认索引为0, 1, 2)
print(df)
df.to_excel('./output.xlsx')
