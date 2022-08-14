

# 总结
# 1、切片：list[idx_beg : idx_end], 其中idx_beg与idx_end可缺省，表示从头（到尾），负数表示倒数xxx
# 2、遍历切片， for lis in list[idx_beg : idx_end]:
# 3、复制列表，拷贝（list[idx_beg : idx_end]）与索引（list）

# 1、切片
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python
# 在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，
# 这将输出分别为0、1和2的元素。
print("========================== 切片")
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3]) # 代码打印该列表的一个切片，其中只包含三名队员
print(players[1:4])
print(players[ :4]) # 你没有指定第一个索引，Python将自动从列表开头开始
print(players[1: ]) # 要让切片终止于列表末尾，也可使用类似的语法
print(players[-3: ])# 负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任何切片，输出名单上的最后三名队员

# 2、遍历切片
# 如果要遍历列表的部分元素，可在for循环中使用切片
# 只遍历前三名队员
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("========================== 遍历切片")
for player in players[ :3]: 
    print(player.title())

# 3、复制列表
# 经常需要根据既有列表创建全新的列表
# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。
# 这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
print("========================== 复制列表（拷贝）")
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[ : ]
print("原始列表: ", my_foods) 
print("复制列表: ", friend_foods)

print("========================== 复制列表（关联）")
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods
friend_foods.append("ice cream")
print("原始列表: ", my_foods) 
print("关联列表: ", friend_foods)

