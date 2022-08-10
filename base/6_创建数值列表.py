
# 小结
# 1、创建数据列表：numbers = list(range(1,6)) 
# 2、数字列表进行统计运算：min, max, sum
# 3、列表解析，squares = [value**2 for value in range(1,11)] 

# 1、创建数值列表
# 将range()作为list()的参数，输出将为一个数字列表
print("========================== range 创建数值列表")
# demo1
for value in range(1,5): 
    print(value)

# demo2
# 函数list()将range()的结果直接转换为列表
numbers = list(range(1,6)) 
print(numbers)

# demo3
# 何创建一个列表，其中包含前10个整数（即1~10）的平方
squares = [] 
for value in range(1,11): 
    squares.append(value**2)
print(squares)

# 2、对数字列表执行简单的统计计算
print("========================== 对数字列表执行简单的统计计算")
print("min", min(squares))
print("max", max(squares))
print("sum", sum(squares))

# 3、列表解析
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
# 首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，
# 并定义一个表达式，用于生成你要存储到列表中的值
# 在这个示例中，表达式为value**2，它计
# 算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号
# for循环为for value in range(1,11)，它将值1~10提供给表达式value**2。请注意，这里的for
# 语句末尾没有冒号。
print("========================== 列表解析")
squares = [value**2 for value in range(1,11)] 
print(squares)