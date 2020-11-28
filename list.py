print("list study\n")
member = ["one", "two", "three", "four"]
print(member)
member.append("five")    #append 仅仅可以添加一个参数
print(member)
member.extend(["six","seven"])    #extend 追加，多个参数
print(member)
member.insert(0,"zero")    #insert 插入，列表从0开始
print(member)

print(member[0])    #获取list元素

####交换list元素####
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member[0],member[1])

#### remove 从列表删除元素 ####
member.remove("one")   #仅仅可以删除一个元素
print(member)

#### del 删除数组元素 ####
del member[0]    #删除元素 0
print(member)

#### pop() 取出list中元素 返回list最后一个元素 ####
print(member.pop())
print(member)

print(member.pop(0))    #从列表中取出 0 号元素
print(member)

#### slice 列表分片，一次取出多个值 ####
print("---- 列表分片，一次取出多个值----")

member = ["zero","one", "two", "three", "four"]
print(member[1:3])
print(member[:3])
print(member[1:])
print(member[:])

#### 列表常用操作符 ####
print("----列表常用操作符----")
print("----列表比较----")
list1 = [123,456,789]
list2 = [123,456]
list3 = [456,123]
list4 = [123,123]
print(list1 > list2)
print(list1 > list3)
print(list2 > list4)
print(list2 < list3)

print("----列表连接----")
list1 = [123,456,789]
list2 = [123,456]
print(list1 + list2)

print("----列表重复操作 * ----")
print(list2 * 3)

print("----列表成员关系 in ----")
print(123 in list1)
print("hello" not in list1)

#### 列表的小伙伴们 ####
print("----列表的小伙伴们----")
print(dir(list))

list5 = [123,456,789,123,123]
print(list5.count(123))