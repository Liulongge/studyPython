import pandas as pd
import matplotlib.pyplot as plt
# 从数学库中导入线性回归
from scipy.stats import linregress

# 将Month数据设置为str格式
sales = pd.read_excel('./15-线性回归_数据预测.xlsx', dtype=({'Month':str}))

print(sales)
slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept
plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='orange')
plt.xticks(sales.index, sales.Month, rotation=90)
# # 使用紧凑布局
plt.title(f'y={slope} * x + {intercept}')
plt.tight_layout()
plt.show()

# 预测
print(slope * 35 + intercept)

# # 使用柱状图显示
# plt.bar(sales.index, sales.Revenue)
# plt.title('Sales')
# plt.xticks(sales.index, sales.Month, rotation=90)
# # 使用紧凑布局
# plt.tight_layout()
# plt.show()

