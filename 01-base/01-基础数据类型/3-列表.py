# 列表让你能够在一个地方存储成组的信息，其中可以只包含几个元素，也可以包含数百万个元素。 
# 列表是新手可直接使用的最强大的Python功能之一，它融合了众多重要的编程概念。

# 列表是什么
# 列表由一系列按特定顺序排列的元素组成。可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；
# 也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
# 鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters 、digits 或names ）是个不错的主意。 
# 在Python中，用方括号 [] 来表示列表，并用逗号来分隔其中的元素。


# 小结
# 1、使用索引值访问，替换列表元素，正数代表从前往后，负数代表从后往前
# 2、append 列表末尾追加元素
# 3、insert 列表中插入元素
# 4、del + 索引值，删除元素
# 5、pop()弹出末尾元素，pop(idx)弹出索引值
# 6、remove 根据元素值删除元素

print("==========================")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 1. 访问列表元素
# 列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
# 要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。 
# 例如，下面的代码从列表bicycles 中提取第一款自行车：
print("========================== 访问列表元素")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # 请求获取列表元素时，Python只返回该元素，而不包括方括号和引号
print(bicycles[2])
# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1 ，可让Python返回最后一个列表元素。
#  。这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。这种约定也适用于其他负数索引。
# 例如，索引-2 返回倒数第 二个列表元素，索引-3 返回倒数第三个列表元素，以此类推
print(bicycles[-1])
print(bicycles[-2])

# 2. 使用列表中的各个值
# 可像使用其他变量一样使用列表中的各个值
print("========================== 使用列表中的各个值")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 3. 修改、添加和删除元素
# 创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。
# 例如，你创建一个游戏，要求玩家射杀从天而降的外星人；为此，可在开始时将一些外星人存储在列表中，
# 然后每当有外星人被射杀时，都将其从列表中删除，而每次有新的外星人出现在屏幕上时，都将其添加到列表中。
# 在整个游戏运行期间，外星人列表的长度将不断变化。
print("========================== 修改、添加和删除元素")
# 3.1 修改列表元素
# 修改列表元素的语法与访问列表元素的语法类似。
# 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。 
# 例如，假设有一个摩托车列表，其中的第一个元素为'honda' ，如何修改它的值呢？
print("========================== 修改")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 
motorcycles[0] = 'ducati' 
print(motorcycles)

# 在列表中添加元素
# 你可能出于众多原因要在列表中添加新元素，例如，你可能希望游戏中出现新的外星人、添
# 加可视化数据或给网站添加新注册的用户
# 在列表末尾添加元素
# 方法append()将元素'ducati'添加到了列表末尾（见），而不影响列表中的其他所有元素
print("========================== 添加 append")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles.append('ducati') 
print(motorcycles)

# 在列表中插入元素
# 使用方法insert()可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值
# 这种操作将列表中既有的每个元素都右移一个位置
print("========================== 插入 insert")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles.insert(0, 'ducati') 
print(motorcycles)

# 从列表中删除元素
# 玩家将空中的一个外星人射杀后，你很可
# 能要将其从存活的外星人列表中删除；当用户在你创建的Web应用中注销其账户时，你需要将该
# 用户从活跃用户列表中删除。你可以根据位置或值来删除列表中的元素
# 使用del语句删除元素
# 使用del可删除任何位置处的列表元素，条件是知道其索引
print("========================== 删除 del")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
del motorcycles[0] 
print(motorcycles)

# 使用方法pop()删除元素
# 方法pop()可删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类
# 比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
print("========================== 删除 pop")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
popped_motorcycle = motorcycles.pop() 
print(motorcycles) 
print(popped_motorcycle)

# 弹出列表中任何位置处的元素
# 你可以使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素
# 的索引即可
print("========================== 删除 pop[idx]")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
first_owned = motorcycles.pop(0) 
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# 根据值删除元素
# 使用remove()从列表中删除元素时，也可接着使用它的值
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要
# 使用循环来判断是否删除了所有这样的值
print("========================== 删除 remove")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles) 
motorcycles.remove('ducati') 
print(motorcycles)