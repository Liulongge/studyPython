
# 总结：
# while
# break
# continue

# for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条件不满足为止。

# 1、使用 while 循环
print("========================== 使用 while 循环")
current_number = 1 
while current_number <= 5: 
    print(current_number) 
    current_number += 1

# 2、让用户选择何时退出
print("========================== 让用户选择何时退出")
# 可使用while循环让程序在用户愿意时不断地运行，如下面的程序parrot.py所示。我们在其中
# 定义了一个退出值，只要用户输入的不是这个值，程序就接着运行：
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 
message = "" 
while message != 'quit': 
    message = input(prompt) 
    print(message) 

# 3、使用标志
print("========================== 使用标志")
# 在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于
# 活动状态。这个变量被称为标志，充当了程序的交通信号灯。
# 你可让程序在标志为True时继续运行，并在任何事件导致标志的值为False时让程序停止运行。这样，在while语句中就只需检查一
# 个条件——标志的当前值是否为True，并将所有测试（是否发生了应将标志设置为False的事件）都放在其他地方，从而让程序变得更为整洁。
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
active = True 
while active: 
    message = input(prompt) 
    if message == 'quit': 
        active = False 
    else: 
        print(message)

# 4、使用 break 退出循环
print("========================== 使用 break 退出循环")
# 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用
# break语句。break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执
# 行，从而让程序按你的要求执行你要执行的代码。
prompt = "\nPlease enter the name of a city you have visited:" 
prompt += "\n(Enter 'quit' when you are finished.) " 
while True: 
    city = input(prompt) 
    if city == 'quit': 
        break
    else: 
        print("I'd love to go to " + city.title() + "!")

# 5、在循环中使用 continue
print("========================== 在循环中使用 continue")
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它
# 不像break语句那样不再执行余下的代码并退出整个循环。
# 来看一个从1数到10，但只打印其中偶数的循环：
current_number = 0 
while current_number < 10: 
    current_number += 1 
    if current_number % 2 == 0: 
        continue 
    print(current_number)

# 6、避免无限循环
print("========================== 避免无限循环")
# 每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。
# 例如，下面的循环从1数到5：
x = 1 
while x <= 5: 
    print(x) 
    x += 1