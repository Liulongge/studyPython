

# 总结：
# 导入单个类：form modular import class
# 从一个模块导入多个类：form modular import class1, class2
# 导入整个模块：import modular
# 导入模块中的所有类：form modular import *


# 导入类
# 随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。
# 为遵循Python的总体理念，应让文件尽可能整洁。
# 为在这方面提供帮助，Python允许你将类存储在模块中，然后在主程序中导入所需的模块。

# 1、导入单个类
# 下面来创建一个只包含Car类的模块。这让我们面临一个微妙的命名问题：在本章中，已经
# 有一个名为car.py的文件，但这个模块也应命名为car.py，因为它包含表示汽车的代码。我们将这
# 样解决这个命名问题：将Car类存储在一个名为car.py的模块中，该模块将覆盖前面使用的文件
# car.py。从现在开始，使用该模块的程序都必须使用更具体的文件名，如my_car.py。下面是模块
# car.py，其中只包含Car类的代码：
print("========================== 导入单个类")
from car import Car 

# import语句让Python打开模块car，并导入其中的Car类
# 导入类是一种有效的编程方式。如果在这个程序中包含了整个Car类，它该有多长呀！通过
# 将这个类移到一个模块中，并导入该模块，你依然可以使用其所有功能，但主程序文件变得整洁
# 而易于阅读了。这还能让你将大部分逻辑存储在独立的文件中；确定类像你希望的那样工作后，
# 你就可以不管这些文件，而专注于主程序的高级逻辑了。
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2、在一个模块中存储多个类
print("========================== 在一个模块中存储多个类")
from car import ElectricCar 
my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
my_tesla.battery.describe_battery() 
my_tesla.battery.get_range()


# 3、从一个模块中导入多个类
print("========================== 从一个模块中导入多个类")
from car import Car, ElectricCar 
my_beetle = Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name()) 
my_tesla = ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())

# 4、导入整个模块
print("========================== 导入整个模块")
import car 
my_beetle = car.Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name()) 
my_tesla = car.ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())

# 5、导入模块中的所有类
print("========================== 导入模块中的所有类")
from car import *

# 6、在一个模块中导入另一个模块
print("========================== 在一个模块中导入另一个模块")
# 有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
# 将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。在这种情况
# 下，可在前一个模块中导入必要的类。