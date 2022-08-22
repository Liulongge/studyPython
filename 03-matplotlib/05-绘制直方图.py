import matplotlib.pyplot as plt
import numpy as np
# 显示中文
import matplotlib.font_manager as fm
my_font = fm.FontProperties(fname = "PingFang.ttc") # 本地路径

# 在x轴绘制定量数据分布特征（直方图）
boxWeight = np.random.randint(0, 10, 100)
x = boxWeight
bins = range(0, 11, 1)
plt.hist(x,  # 输入连续性数据
         bins=bins,  # 柱体个数或者柱体边缘范围
         color='g',
         histtype='bar',  # 柱体类型
         rwidth=1,  # 柱体宽度
         alpha=0.6)
plt.xlabel("箱子编号", fontproperties = my_font)
plt.ylabel("箱子重量（kg）", fontproperties = my_font)
plt.show()