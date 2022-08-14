
# 总结：
# 存储数据使用json, import json
# json.dump(数据, 文件)：存储数据
# json.load(文件)：加载数据 

# 很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。
# 不管专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。
# 用户关闭程序时，你几乎总是要保存他们提供的信息；一种简单的方式是使用模块json来存储数据。
# 模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
# 你还可以使用json在Python程序之间分享数据。更重要的是，JSON数据格式并非Python专用的，
# 这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。
# 这是一种轻便格式，很有用，也易于学习。

# 注意 JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用。

# 1、使用 json.dump()和 json.load()

# 我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。
# 第一个程序将使用json.dump()来存储这组数字，而第二个程序将使用json.load()。
# 函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。

# 我们先导入模块json，再创建一个数字列表。我们指定了要将该数字列表存储到其中的文件的名称。
# 通常使用文件扩展名.json来指出文件存储的数据为JSON格式。
# 接下来，我们以写入模式打开这个文件，让json能够将数据写入其中。
# 我们使用函数json.dump()将数字列表存储到文件numbers.json中。
print("========================== 使用 json.dump()")
import json 
numbers = [2, 3, 5, 7, 11, 13] 
filename = 'numbers.json' 
with open(filename, 'w') as f_obj: 
    json.dump(numbers, f_obj)

print("========================== 使用 json.load()")
import json 
filename = 'numbers.json' 
with open(filename) as f_obj: 
    numbers = json.load(f_obj) 
    print(numbers)


# 2、保存和读取用户生成的数据
print("========================== 保存和读取用户生成的数据")
# 对于用户生成的数据，使用json保存它们大有裨益，因为如果不以某种方式进行存储，
# 等程序停止运行时用户的信息将丢失。下面来看一个这样的例子：用户首次运行程序时被提示输入自己的名字，这样再次运行程序时就记住他了。
print("========================== 保存和读取用户生成的数据(保存)")
import json 
username = input("What is your name? ") 
filename = 'username.json' 
with open(filename, 'w') as f_obj: 
    json.dump(username, f_obj) 
    print("We'll remember you when you come back, " + username + "!")

print("========================== 保存和读取用户生成的数据(读取)")
import json 
filename = 'username.json' 
with open(filename) as f_obj: 
    username = json.load(f_obj) 
    print("Welcome back, " + username + "!")

# 3、重构
print("========================== 重构")
# 你经常会遇到这样的情况：代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。
# 这样的过程被称为重构。重构让代码更清晰、更易于理解、更容易扩展。
import json 
def get_stored_username(): 
    """如果存储了用户名，就获取它""" 
    filename = 'username.json' 
    try: 
        with open(filename) as f_obj: 
            username = json.load(f_obj) 
    except FileNotFoundError: 
        return None 
    else: 
        return username 

def greet_user(): 
    """问候用户，并指出其名字""" 
    username = get_stored_username() 
    if username: 
        print("Welcome back, " + username + "!") 
    else: 
        username = input("What is your name? ") 
        filename = 'username.json' 
        with open(filename, 'w') as f_obj: 
            json.dump(username, f_obj) 
            print("We'll remember you when you come back, " + username + "!") 

greet_user()