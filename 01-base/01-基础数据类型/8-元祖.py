
# 总结：
# 1、元祖的元素不可更改
# 2、元祖变量本身可以修改

# 列表非常适合用于存储在程序运行期间可能变化的数据集, 列表是可以修改的
# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

# 1、定义元组
# 元组看起来犹如列表，但使用圆括号()而不是方括号[]来标识。
# 定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
print("========================== 定义元祖")
dimensions = (200, 50) 
print(dimensions[0]) 
print(dimensions[1])

# 2、遍历元组中的所有值
print("========================== 遍历元组中的所有值")
dimensions = (200, 50) 
for dimension in dimensions: 
    print(dimension)

# 3、修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺
# 寸，可重新定义整个元组：
print("========================== 修改元组变量")
dimensions = (200, 50)
print("原始值:") 
for dimension in dimensions: 
    print(dimension) 
dimensions = (400, 100) 
print("修改后值:") 
for dimension in dimensions: 
    print(dimension)