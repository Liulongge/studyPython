
# 总结
# 1、if 条件 :

# 2、if 条件 :
#    else :

# 3、if 条件 :
#    elif 条件 :
#    else :

# 4、if 条件 :
#    elif 条件 :
#    elif 条件 :
#    else :

# 5、if 条件 :
#    if 条件 :
#    if 条件 :

# if conditional_test: 
# do something

age = 19 
if age >= 18: 
    print("You are old enough to vote!")

# 1、简单的 if 语句
print("========================== if 语句")
age = 19
if age >= 18: 
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")

# 2、简单的 if-else 语句
print("========================== if-else语句")
age = 17 
if age >= 18: 
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote.") 
    print("Please register to vote as soon as you turn 18!")

# 3、if-elif-else 结构
print("========================== if-elif-else语句")
age = 12 
if age < 4: 
    print("Your admission cost is $0.") 
elif age < 18: 
    print("Your admission cost is $5.") 
else: 
    print("Your admission cost is $10.")

# 4、使用多个 elif 代码块
print("========================== 多个 elif 代码块")
age = 12 
if age < 4: 
    price = 0 
elif age < 18: 
    price = 5 
elif age < 65: 
    price = 10 
else: 
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 5、省略 else 代码块
print("========================== 省略 else 代码块")
age = 12 
if age < 4: 
    price = 0 
elif age < 18: 
    price = 5 
elif age < 65: 
    price = 10 
elif age >= 65: 
    price = 5 
print("Your admission cost is $" + str(price) + ".")

# 6、测试多个条件
print("========================== 测试多个条件")
requested_toppings = ['mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.") 
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.") 
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.") 
print("Finished making your pizza!")