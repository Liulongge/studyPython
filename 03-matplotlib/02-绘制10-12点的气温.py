
import random
from matplotlib import pyplot as plt  # 导入pyplot

# 1、显示中文
import matplotlib.font_manager as fm
# my_font = fm.FontProperties(fname = "/System/Library/Fonts/PingFang.ttc") # 系统路径
my_font = fm.FontProperties(fname = "PingFang.ttc") # 本地路径
fig = plt.figure(figsize = (20, 8), dpi = 80)
x = range(0, 120)

y = [random.randint(20, 35) for i in range(120)] # 列表解析，产生一个元素个数为120，范围为20-35的列表

plt.plot(x, y)
# 2、调整x轴刻度
_x = list(x)
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::6], _xticks_labels[::6], rotation = 40, fontproperties = my_font) # 数字和字符串一一对应, 取步长3, 标签旋转

# 3、添加描述信息
plt.xlabel("时间", fontproperties = my_font)
plt.ylabel("温度/摄氏度", fontproperties = my_font)
plt.title("10-12点温度变化曲线", fontproperties = my_font)
plt.show()