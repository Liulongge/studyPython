

# 总结：
# input(): 获取用户输入，并打印提示语
# int(): 将字符转换为整数


# 大多数程序都旨在解决最终用户的问题，为此通常需要从用户那
# 里获取一些信息


# 1、函数 input()的工作原理
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在
# 一个变量中，以方便你使用。

# 函数input()接受一个参数：即要向用户显示的提示或说明，让用户知道该如何
print("========================== input()的工作原理")
message = input("Tell me something, and I will repeat it back to you: ") 
print(message)

# 使用 int()来获取数值输入
print("========================== 使用 int()来获取数值输入")
# 使用函数input()时，Python将用户输入解读为字符串
# 函数int()将数字的字符串表示转换为数值表示
age = input("How old are you? ") 
print(int(age)) 

# 求模运算符
print("========================== 求模运算符")
# 处理数值信息时，求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数
# 求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。
# 如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。你可利用这一点来判
# 断一个数是奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ") 
number = int(number) 
if number % 2 == 0: 
    print("\nThe number " + str(number) + " is even.") 
else: 
    print("\nThe number " + str(number) + " is odd.")

