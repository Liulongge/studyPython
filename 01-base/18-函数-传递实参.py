

# 总结：
# 位置实参
# 关键字实参
# 默认值
# 等效的函数调用
# 让实参变得可选

# 函数是带名字的代码块，用于完成具体的工作。
# 要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用
# 执行该任务的函数，让Python运行其中的代码。

# 1、定义函数
# 文本是被称为文档字符串(docstring）的注释，描述了函数是做什么的。
# 文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
print("========================== 定义函数")
def greet_user(): 
    """显示简单的问候语""" 
    print("Hello!") 

greet_user()

# 向函数传递信息
print("========================== 向函数传递信息")
def greet_user(username): 
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!") 

greet_user("jesse")

# 实参和形参
# 在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信
# 息。在代码greet_user('jesse')中，值'jesse'是一个实参。实参是调用函数时传递给函数的信
# 息。我们调用函数时，将要让函数使用的信息放在括号内。在greet_user('jesse')中，将实参
# 'jesse'传递给了函数greet_user()，这个值被存储在形参username中。


# 2、传递实参
# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参
# 的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；也可使用关键字实参，其
# 中每个实参都由变量名和值组成；还可使用列表和字典。
print("========================== 传递实参")
# 2.1、位置实参
print("========================== 传递实参(位置实参)")
# Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，
# 最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参
def describe_pet(animal_type, pet_name): 
    """显示宠物的信息""" 
    print("I have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".") 

describe_pet('hamster', 'harry')

# 2.2、关键字实参
print("========================== 传递实参(关键字实参)")
# 关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆。
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
# 注意：使用关键字实参时，务必准确地指定函数定义中的形参名。
def describe_pet(animal_type, pet_name): 
    """显示宠物的信息""" 
    print("I have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".") 
    
describe_pet(pet_name='harry', animal_type='hamster')

# 2.3、默认值
print("========================== 传递实参(默认值)")
# 编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用
# 指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略
# 相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
# 注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
# 这让Python依然能够正确地解读位置实参。
def describe_pet(pet_name, animal_type='dog'): 
    """显示宠物的信息""" 
    print("I have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# 2.4、等效的函数调用
print("========================== 传递实参(等效的函数调用)")
# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息""" 
    print("I have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 一条名为Willie的小狗
describe_pet('willie') 
describe_pet(pet_name='willie') 
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster') 
describe_pet(pet_name='harry', animal_type='hamster') 
describe_pet(animal_type='hamster', pet_name='harry')


# 2.5、让实参变成可选的
print("========================== 让实参变成可选的")
# 有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。
# 可使用默认值来让实参变成可选的。
# 并非所有的人都有中间名，但如果你调用这个函数时只提供了名和姓，它将不能正确
# 地运行。为让中间名变成可选的，可给实参middle_name指定一个默认值——空字符串，并在用
# 户没有提供中间名时不使用这个实参。为让get_formatted_name()在没有提供中间名时依然可行，
# 可给实参middle_name指定一个默认值——空字符串，并将其移到形参列表的末尾：
def get_formatted_name(first_name, last_name, middle_name=''): 
    """返回整洁的姓名""" 
    if middle_name: 
        full_name = first_name + ' ' + middle_name + ' ' + last_name 
    else: 
        full_name = first_name + ' ' + last_name 
    return full_name.title() 

musician = get_formatted_name('jimi', 'hendrix') 
print(musician) 
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)