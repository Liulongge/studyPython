
# 总结
# 1、sort 进行永久性排序，参数reverse=True 进行反向排序
# 2、sorted 进行临时性排序，参数reverse=True 进行反向排序
# 3、reverse 进行永久性顺心翻转
# 4、len 求取长度


print("========================== 排序")
# 使用方法 sort()对列表进行永久性排序
print("========================== 正向永久性排序")
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars)
cars.sort()
print(cars)

# 按与字母顺序相反的顺序排列列表元素，为此，只需向sort()方法传递参数reverse=True。
print("========================== 反向永久性排序")
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars)
cars.sort(reverse = True)
print(cars)


# sorted()对列表进行临时排序
# 调用函数sorted()后，列表元素的排列顺序并没有变（见）。如果你要按与字母顺
# 序相反的顺序显示列表，也可向函数sorted()传递参数reverse=True。
print("========================== 正向临时性排序")
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars)
print(sorted(cars))
print(cars)

# 倒着打印列表
print("========================== 反转列表元素的排列顺序")
# reverse()反转列表元素的排列顺序
# reverse()永久性地修改列表元素的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars) 
cars.reverse() 
print(cars)

# 确定列表的长度
# 函数len()可快速获悉列表的长度
print("========================== 获取列表长度")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))