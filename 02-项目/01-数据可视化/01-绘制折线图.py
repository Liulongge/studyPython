

# 数据可视化指的是通过可视化表示来探索数据，它与数据挖掘紧密相关，而数据挖掘指的是使用代码来探索数据集的规律和关联。
# 数据集可以是用一行代码就能表示的小型数字列表，也可以是数以吉字节的数据。

# 最流行的工具之一是matplotlib，它是一个数学绘图库，我们将使用它来制作简单的图表，如折线图和散点图。
# 1、绘制简单的折线图
print("========================== 绘制简单的折线图")
import matplotlib.pyplot as plt 
squares = [1, 4, 9, 16, 25]
plt.plot(squares) 
plt.show()

# 2、修改标签文字和线条粗细
# 函数xlabel()和ylabel()让你能够为每条轴设置标题
# 函数tick_params()设置刻度的样式，其中指定的实参将影响x轴和y轴上的刻度（axes='both'），并将刻度标记的字号设置为14（labelsize=14）

print("========================== 修改标签文字和线条粗细")
import matplotlib.pyplot as plt 
squares = [1, 4, 9, 16, 25] 
plt.plot(squares, linewidth=5) 
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()


# 3、校正图形
# 图形更容易阅读后，我们发现没有正确地绘制数据：折线图的终点指出4.0的平方为25！下面来修复这个问题。
# 当你向plot()提供一系列数字时，它假设第一个数据点对应的x坐标值为0，但我们的第一个点对应的x值为1。
# 为改变这种默认行为，我们可以给plot()同时提供输入值和输出值：
print("========================== 校正图形")
import matplotlib.pyplot as plt 
input_values = [1, 2, 3, 4, 5] 
squares = [1, 4, 9, 16, 25] 
plt.plot(input_values, squares, linewidth=5)
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

# 4、使用 scatter()绘制一系列点
print("========================== 使用 scatter()绘制一系列点")
# 有时候，需要绘制散点图并设置各个数据点的样式。例如，你可能想以一种颜色显示较小的值，而用另一种颜色显示较大的值。
# 绘制大型数据集时，你还可以对每个点都设置同样的样式，再使用不同的样式选项重新绘制某些点，以突出它们。
import matplotlib.pyplot as plt 
x_values = [1, 2, 3, 4, 5] 
y_values = [1, 4, 9, 16, 25] 
# 自定义颜色
# 你还可以使用RGB颜色模式自定义颜色。要指定自定义颜色，可传递参数c，并将其设置为一个元组，
# 其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。例如，下面的代码行创建一个由淡蓝色点组成的散点图：
#  c=(0, 0, 0.8)

# 删除数据点的轮廓
# matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的
# 数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，
# 可在调用scatter()时传递实参edgecolor='none'：
# plt.scatter(x_values, y_values, edgecolor='none', s=40)
plt.scatter(x_values, y_values, c='red' ,s=100,  edgecolor='none') 
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.show()

# 5、使用颜色映射
# 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律，
# 例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。
# 模块pyplot内置了一组颜色映射。要使用这些颜色映射，你需要告诉pyplot该如何设置数据集中每个点的颜色。
# 下面演示了如何根据每个点的y值来设置其颜色：
print("========================== 使用颜色映射")
import matplotlib.pyplot as plt 
x_values = list(range(1001)) 
y_values = [x**2 for x in x_values] 
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14) 
print("========================== 自动保存图表")
# 自动保存图表
# 第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的
# 目录中；第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参。
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
