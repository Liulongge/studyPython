

# 总结：
# 传递列表
# 函数中可以修改入参列表，函数外可以感知到(类似c++指针？)
# 使用列表切片list[:]，传递副本，影响不到list本身


# 1、传递列表
print("========================== 传递列表")
# 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对
# 象（如字典）。将列表传递给函数后，函数就能直接访问其内容。下面使用函数来提高处理列表的效率。
def greet_users(names): 
    """向列表中的每位用户都发出简单的问候""" 
    for name in names: 
        msg = "Hello, " + name.title() + "!" 
        print(msg) 

usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)

# 2、在函数中修改列表
print("========================== 在函数中修改列表")
# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永
# 久性的，这让你能够高效地处理大量的数据
# 首先创建一个列表，其中包含一些要打印的设计
def print_models(unprinted_designs, completed_models): 
    """ 
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """ 
    while unprinted_designs: 
        current_design = unprinted_designs.pop() 
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design) 
        completed_models.append(current_design)

def show_completed_models(completed_models): 
    """显示打印好的所有模型""" 
    print("the following models have been printed:") 
    for completed_model in completed_models: 
        print(completed_model) 

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 
print_models(unprinted_designs, completed_models) 
show_completed_models(completed_models)
print("unprinted_designs被操作后： ", unprinted_designs)


# 3、禁止函数修改列表
print("========================== 禁止函数修改列表")
# 有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列
# 表，并编写了一个将这些设计移到打印好的模型列表中的函数。你可能会做出这样的决定：即便
# 打印所有设计后，也要保留原来的未打印的设计列表，以供备案。但由于你将所有的设计都移出
# 了unprinted_designs，这个列表变成了空的，原来的列表没有了。为解决这个问题，可向函数传
# 递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
def print_models(unprinted_designs, completed_models): 
    """ 
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """ 
    while unprinted_designs: 
        current_design = unprinted_designs.pop() 
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design) 
        completed_models.append(current_design)

def show_completed_models(completed_models): 
    """显示打印好的所有模型""" 
    print("the following models have been printed:") 
    for completed_model in completed_models: 
        print(completed_model) 

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 
print_models(unprinted_designs[ : ], completed_models) 
show_completed_models(completed_models)
print("unprinted_designs被操作后： ", unprinted_designs)