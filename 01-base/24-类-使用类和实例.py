

# 1、使用类和实例
# 你可以使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间都将花在使用根
# 据类创建的实例上。你需要执行的一个重要任务是修改实例的属性。你可以直接修改实例的属性，
# 也可以编写方法以特定的方式进行修改。
print("========================== 使用类和实例")
class Car(): 
    """一次模拟汽车的简单尝试""" 
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title() 

my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())

# 2、给属性指定默认值
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。
# 在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的；
# 如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
print("========================== 给属性指定默认值")
class Car(): 
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year
        self.odometer_reading = 0 
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title() 
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.") 
    def update_odometer(self, mileage): 
        """将里程表读数设置为指定的值""" 
        self.odometer_reading = mileage
    def increment_odometer(self, miles): 
        """将里程表读数增加指定的量""" 
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()

# 3、修改属性的值
print("========================== 修改属性的值(直接通过实例进行修改)")
# 可以以三种不同的方式修改属性的值：直接通过实例进行修改；通过方法进行设置；通过方法进行递增（增加特定的值）。
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

print("========================== 修改属性的值( 通过方法修改属性的值)")
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 
my_new_car.update_odometer(27) 
my_new_car.read_odometer()

print("========================== 修改属性的值(通过方法对属性的值进行递增)")
my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name()) 
my_used_car.update_odometer(23500) 
my_used_car.read_odometer() 
my_used_car.increment_odometer(100) 
my_used_car.read_odometer()


