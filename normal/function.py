def myFirstFunction():
    print("这是我的第一个函数")
    print("感谢CCTV")
    return 0;

def mySecondFunction(name):
    print(name + "我爱你")
    return 0;

def add(num1, num2):
    result = num1 + num2
    print(result)
    return 0

def mult(num1, num2):
    return num1 * num2

def func():
    "函数文档"
    print("尝试写函数文档")
    return 0

def saySome(name, words):
    print(name, "->", words)
    return 0

def saySomeThing(name = "我爱", words = "世界和平"):
    print(name, "->", words)
    return 0


myFirstFunction()
mySecondFunction("祖国")
add(8, 5)
print(mult(8, 5))
help(func)
print(func.__doc__)
saySome(words = "世界和平", name = "我爱")

saySomeThing()
saySomeThing(name = "她爱")
saySomeThing(words = "我")

#### 收集参数 ####
def test(*params):
    print("参数长度: ", len(params))
    print("第二个参数: ", params[1])
    return 0

test(1, "Hello", 2, 3)