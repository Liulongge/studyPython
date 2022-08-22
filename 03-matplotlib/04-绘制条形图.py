

'''
直方图描述连续型数据分布，定量
柱状图描述离散数据分布，定性
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
# 显示中文
import matplotlib.font_manager as fm
my_font = fm.FontProperties(fname = "PingFang.ttc") # 本地路径


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# 在x轴上绘制定性数据分布特征（柱状图）
plt.bar(x,  # 柱状图柱体标签值
        y,  # 柱体高度
        align='center',  # 柱体对齐方式
        color='c', # 柱体颜色
        tick_label=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i'],  # 刻度标签值
        hatch='/')   # 填充样式，越密集填充就越密

plt.xlabel("箱子编号", fontproperties = my_font)
plt.ylabel("箱子重量（kg）", fontproperties = my_font)
plt.show()
