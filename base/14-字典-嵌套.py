
# 总结：
# 字典列表：将字典存储于列表中
# 字典中存储列表
# 字典中存储字典

# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。你
# 可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

# 1、字典列表 -- 由字典组成的列表，字典存储于列表中
# 字典alien_0包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上
# 全部外星人的信息了。如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每
# 个外星人都是一个字典，包含有关该外星人的各种信息。
print("========================== 字典列表")
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15} 
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens: 
    print(alien)

print("========================== 自动生成字典列表")
# 创建一个用于存储外星人的空列表
aliens = [] 
# 创建30个绿色的外星人
for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
    aliens.append(new_alien) 
# 显示前五个外星人
for alien in aliens[:5]: 
    print(alien) 
print("...") 
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))


# 2、在字典中存储列表
# 列表存储于字典中
print("========================== 在字典中存储列表")
# 例如，你如何描述顾客点的比萨呢？如果使用列表，只能存储要添加的比萨配料；但如果使用字典，就不仅可在其中包含
# 配料列表，还可包含其他有关比萨的描述。
# 在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。其中的配料列表是一个
# 与键'toppings'相关联的值。要访问该列表，我们使用字典名和键'toppings'，就像访问字典中
# 的其他值一样。这将返回一个配料列表，而不是单个值：
# 存储所点比萨的信息
pizza = { 
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'], 
} 
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:") 
for topping in pizza['toppings']: 
    print("\t" + topping)

# 3、在字典中存储字典
print("========================== 在字典中存储字典表")
# 可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网站用户，
# 每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，
# 并将该字典作为与用户名相关联的值。在下面的程序中，对于每位用户，我们都存储了其三项信
# 息：名、姓和居住地；为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关联的
# 信息字典
users = { 
    'aeinstein': { 
    'first': 'albert', 
    'last': 'einstein', 
    'location': 'princeton', 
    }, 
    'mcurie': { 
    'first': 'marie', 
    'last': 'curie', 
    'location': 'paris', 
    }, 
} 
for username, user_info in users.items(): 
    print("Username: " + username)
    full_name = user_info['first'] + " " + user_info['last'] 
    location = user_info['location'] 
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())