


# 继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；
# 原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

# 子类的方法__init__()
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。
# 为此，子类的方法__init__()需要父类施以援手。
# a. 首先是Car类的代码，创建子类时，父类必须包含在当前文件中，且位于子类前面
# b. 定义子类ElectricCar。定义子类时，必须在括号内指定父类的名称
# c. super()是一个特殊函数，帮助Python将父类和子类关联起来。
#    这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性。
#    父类也称为超类（superclass），名称super因此而得名。
print("========================== 继承")
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self): 
        """电动汽车没有油箱""" 
        print("This car need a gas tank!")

class ElectricCar(Car): 
    """电动汽车的独特之处""" 
    def __init__(self, make, model, year): 
        """初始化父类的属性""" 
        super().__init__(make, model, year) 

my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name())


# 给子类定义属性和方法
print("========================== 给子类定义属性和方法")
# 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。
# 下面来添加一个电动汽车特有的属性（电瓶），以及一个描述该属性的方法。我们将存储电瓶容量，并编写一个打印电瓶描述的方法：
class ElectricCar2(Car): 
    """Represent aspects of a car, specific to electric vehicles.""" 
    def __init__(self, make, model, year): 
        """ 电动汽车的独特之处初始化父类的属性，再初始化电动汽车特有的属性 """ 
        super().__init__(make, model, year) 
        self.battery_size = 70 
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 

my_tesla = ElectricCar2('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
my_tesla.describe_battery()


# 重写父类的方法
print("========================== 重写父类的方法")
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。
# 为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
# 这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
# 假设Car类有一个名为fill_gas_tank()的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：

class ElectricCar3(Car):
    """Represent aspects of a car, specific to electric vehicles.""" 
    def __init__(self, make, model, year): 
        """ 电动汽车的独特之处初始化父类的属性，再初始化电动汽车特有的属性 """ 
        super().__init__(make, model, year) 
    def fill_gas_tank(self): 
        """电动汽车没有油箱""" 
        print("This car don't need a gas tank!")

my_tesla = ElectricCar3('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
my_tesla.fill_gas_tank()

# 将实例用作属性
print("========================== 将实例用作属性")
# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。
# 在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。你可以将大型类拆分成多个协同工作的小类
# 例如，不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。
# 在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为Battery的类中，并将一个Battery实例用作ElectricCar类的一个属性：

class Battery(): 
    """一次模拟电动汽车电瓶的简单尝试""" 
    def __init__(self, battery_size=70):
        """初始化电瓶的属性""" 
        self.battery_size = battery_size 
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 

class ElectricCar(Car): 
    """电动汽车的独特之处""" 
    def __init__(self, make, model, year): 
        """ 初始化父类的属性，再初始化电动汽车特有的属性 """ 
        super().__init__(make, model, year) 
        self.battery = Battery() 

my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
my_tesla.battery.describe_battery()