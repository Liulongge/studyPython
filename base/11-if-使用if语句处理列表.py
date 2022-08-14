

# 1、检查特殊元素
print("========================== 检查特殊元素")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings : 
    if requested_topping == 'green peppers' :  # 检查特殊元素
        print("Sorry, we are out of green peppers right now.") 
    else:
        print("Adding " + requested_topping + ".") 
print("\nFinished making your pizza!")

# 2、确定列表不是空的
print("========================== 确定列表不是空的")
requested_toppings = [] 
if requested_toppings : # 确定列表不是空的
    for requested_topping in requested_toppings: 
        print("Adding " + requested_topping + ".") 
        print("\nFinished making your pizza!") 
    else: 
        print("Are you sure you want a plain pizza?")

# 3、使用多个列表
# 顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸薯条，该
# 怎么办呢？可使用列表和if语句来确定能否满足顾客的要求。
# 来看看在制作比萨前如何拒绝怪异的配料要求。下面的示例定义了两个列表，其中第一个列
# 表包含比萨店供应的配料，而第二个列表包含顾客点的配料。这次对于requested_toppings中的
# 每个元素，都检查它是否是比萨店供应的配料，再决定是否在比萨中添加它：
print("========================== 使用多个列表")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] 
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: 
        print("Adding " + requested_topping + ".") 
    else: 
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")





