
# 总结：
# 1、导入整个模块：import model
# 2、倒入特定函数：from module_name import function_name
# 3、使用as给函数指定别名：from module_name import function_name as fn
# 4、使用 as 给模块指定别名：import module_name as mn
# 5、导入模块中的所有函数：from module_name import *

# 将函数存储在模块中
# 函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。
# 你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。
# import语句允许在当前运行的程序文件中使用模块中的代码。
# 通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。
# 这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。
# 知道如何导入函数还能让你使用其他程序员编写的函数库。

# 1、导入整个模块
# 要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码。
# 下面来创建一个包含函数make_pizza()的模块。

# Python读取这个文件时，代码行import pizza让Python打开文件pizza.py，并将其中的所有函
# 数都复制到这个程序中。你看不到复制的代码，因为这个程序运行时，Python在幕后复制这些代
# 码。你只需知道，在making_pizzas.py中，可以使用pizza.py中定义的所有函数。
print("========================== 导入整个模块")
import pizza 
pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 2、导入特定的函数
print("========================== 导入特定的函数")
# 你还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2

# 若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数
# make_pizza()，因此调用它时只需指定其名称。
from pizza import make_pizza 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 3、使用 as 给函数指定别名
print("========================== 使用 as 给函数指定别名")
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短
# 而独一无二的别名——函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
# from module_name import function_name as fn
from pizza import make_pizza as mp 
mp(16, 'pepperoni') 
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 4、使用 as 给模块指定别名
print("========================== 使用 as 给模块指定别名")
# 你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p），让你
# 能够更轻松地调用模块中的函数。相比于pizza.make_pizza()，p.make_pizza()更为简洁：
# import module_name as mn
import pizza as p 
p.make_pizza(16, 'pepperoni') 
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5、导入模块中的所有函数
# 使用星号（*）运算符可让Python导入模块中的所有函数：
# from module_name import *
print("========================== 导入模块中的所有函数")
from pizza import * 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
