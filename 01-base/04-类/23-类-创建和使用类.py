
# 总结：
# 方法__init__(self)在实例化类是自动调用
# 访问属性和调用方法使用“.”
# self：每个与类相关联的方法
# 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。

# 类编码风格：
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
# 实例名和模块名都采用小写格式，并在单词之间加上下划线。
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的
# 功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，
# 对其中的类可用于做什么进行描述。

# 1、创建和使用类
# __init__(): 方法__init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。
# 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。

# self: 形参self必不可少，必须位于其他形参的前面。
# Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。
# 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
print("========================== 创建和使用类")
class Dog(): 
    """一次模拟小狗的简单尝试""" 
    def __init__(self, name, age): 
        """初始化属性name和age""" 
        self.name = name 
        self.age = age 
    def sit(self): 
        """模拟小狗被命令时蹲下""" 
        print(self.name.title() + " is now sitting.") 
    def roll_over(self): 
        """模拟小狗被命令时打滚""" 
        print(self.name.title() + " rolled over!")

# 2、根据类创建实例
my_dog = Dog('willie', 6)
# 访问属性“.” 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")
# 调用方法“.”
my_dog.sit() 
my_dog.roll_over()
# 创建多个实例
your_dog = Dog('lucy', 3) 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")

