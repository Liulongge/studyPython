
# 总结：
# 方法__init__(self)在实例化类是自动调用
# 访问属性和调用方法使用“.”
# self：每个与类相关联的方法
# 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。

# 面向对象编程是最有效的软件编写方法之一。
# 基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独
# 特的个性。使用面向对象编程可模拟现实情景，其逼真程度达到了令你惊讶的地步。
# 根据类来创建对象被称为实例化，这让你能够使用类的实例。

# 1、创建和使用类
# 方法__init__()
# 类中的函数称为方法；
# 方法__init__()是一个特殊的方法，每当你根据Dog类创建新实
# 例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约
# 定，旨在避免Python默认方法与普通方法发生名称冲突。

# 形参self必不可少，还必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？因为
# Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
# 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
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