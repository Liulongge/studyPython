

# 小结
# 1、for循环
# for name in 列表 :
#    循环体

# 遍历整个列表
print("========================== 遍历打印列表中元素")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)

# 深入地研究循环
# 在 for 循环中执行更多的操作
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

