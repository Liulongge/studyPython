

# 总结：
# 返回简单值
# 返回字典
# 返回列表

# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回
# 的值被称为返回值。在函数中，可使用return语句将值返回到调用函数的代码行。返回值让你能
# 够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

# 1、返回简单值
print("========================== 返回简单值")
def get_formatted_name(first_name, last_name): 
    """返回整洁的姓名""" 
    full_name = first_name + ' ' + last_name 
    return full_name.title() 

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)


# 2、返回字典
print("========================== 返回字典")
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
def build_person(first_name, last_name): 
    """返回一个字典，其中包含有关一个人的信息""" 
    person = {'first': first_name, 'last': last_name} 
    return person 

musician = build_person('jimi', 'hendrix') 
print(musician)
