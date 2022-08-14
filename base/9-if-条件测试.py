

# 总结
# 条件测试关键词： ==, !=, >=, and, or, in, not in
# 1、if语句，简单demo
print("========================== if语句demo")
cars = ['audi', 'bmw', 'subaru', 'toyota'] 
for car in cars: 
    if car == 'bmw': 
        print(car.upper()) 
    else: 
        print(car.title())

# 2、条件测试
# 每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。Python
# 根据条件测试的值为True还是False来决定是否执行if语句中的代码。如果条件测试的值为True，
# Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。

# 2.1、检查是否相等
car = 'BMW'
print(car == 'BMW')

# 2.2、检查是否相等时不考虑大小写
car = 'BMW'
print(car.lower() == 'bmw')

# 2.3、检查是否不相等
requested_topping = 'mushrooms' 
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")

# 2.4、比较数字
age = 18
print(age == 18)

# 2.5、检查多个条件
# 2.5.1、使用and检查多个条件
age_0 = 22 
age_1 = 18 
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))

# 2.5.2、使用or检查多个条件
age_0 = 22 
age_1 = 18 
print(age_0 >= 21 or age_1 >= 21)
print((age_0 >= 21) or (age_1 >= 21))

# 2.6、检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
print('mushrooms' in requested_toppings)

# 2.7、检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie' 
print(user not in banned_users)

# 2.8、布尔表达式
game_active = True 
can_edit = False