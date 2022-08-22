# 总结：
# 1、绘制折线图 plt.plot
# 2、设置图像大小和分辨率 plt.figure
# 3、实现图像存储 plt.savefig
# 4、设置x/y轴刻度和字符串 xticks/yticks
# 5、解决刻度稀疏和稠密问题 xticks/yticks
# 6、设置x/y轴的lable title、xlable、ylable
# 7、设置字体 FontProperties
# 8、一个图上绘制多个图形 plt多次plot
# 9、绘制散点图 plt.scatter()
# 10、绘制条形图 plt.bar()
# 11、绘制直方图 plt.hist()

from matplotlib import pyplot as plt  # 导入pyplot

# 1、设置图片大小
# def figure(num=None,  # autoincrement if None, else integer from 1-N
#            figsize=None,  # defaults to rc figure.figsize
#            dpi=None,  # defaults to rc figure.dpi
#            facecolor=None,  # defaults to rc figure.facecolor
#            edgecolor=None,  # defaults to rc figure.edgecolor
#            frameon=True,
#            FigureClass=Figure,
#            clear=False,
#            **kwargs
#            ):
# 通过实例化一个figure并且传递参数，能够在后台自动使用figure实例
# 在图像模糊时候，可以使用dpi（每英寸点的个数）参数让图像更清晰
fig = plt.figure(figsize = (20, 8), dpi = 50)
x = range(2, 26, 2)

y = [15, 13, 14.5, 17, 20, 15, 26, 26, 24, 22, 18, 15]

plt.plot(x, y) # 传入x, y通过plot绘制出折线图
# 2、设置x轴刻度
_xtick_labels = [ (val /  2) for val in range(4, 49)] # 列表解析
plt.xticks(_xtick_labels[::3]) # 列表取步长操作
plt.yticks(range(min(y), max(y) + 1)) # 列表取步长操作

plt.savefig("./01-demo.svg") # 保存图片，可以保存为svg矢量图格式，放大不会有锯齿
plt.savefig("./01-demo.jpg") # 保存图片
plt.show() # 在执行程序时候展示图像
