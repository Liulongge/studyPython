
# 总结：
# 传递任意数量实参 *param
# 使用任意数量的关键字实参 **param


# 1、传递任意数量的实参
# 有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
print("========================== 传递任意数量的实参")
# 例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配
# 料。下面的函数只有一个形参*toppings，但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：
# 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封
# 装到这个元组中。函数体内的print语句通过生成输出来证明Python能够处理使用一个值调用函
# 数的情形，也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用，注意，
# Python将实参封装到一个元组中，即便函数只收到一个值也如此：
def make_pizza(*toppings): 
    """概述要制作的比萨""" 
    print("Making a pizza with the following toppings:") 
    for topping in toppings: 
        print("+ " + topping) 

make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参
print("========================== 结合使用位置实参和任意数量实参")
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最
# 后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza(size, *toppings): 
    """概述要制作的比萨""" 
    print("Making a " + str(size) + 
    "-inch pizza with the following toppings:") 
    for topping in toppings: 
        print("+ " + topping) 

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
print("========================== 使用任意数量的关键字实参")
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种
# 情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
# 一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。
# 在下面的示例中，函数build_profile()接受名和姓，同时还接受任意数量的关键字实参：
def build_profile(first, last, **user_info): 
    """创建一个字典，其中包含我们知道的有关用户的一切""" 
    profile = {} 
    profile['first_name'] = first 
    profile['last_name'] = last 
    for key, value in user_info.items():
        profile[key] = value 
    return profile 

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') 
print(user_profile)

