
# 总结：
# items()遍历键-值对
# keys()遍历所有键，按顺序遍历所有键sorted()
# values()遍历所有值，剔除重复项set()

# 一个Python字典可能只包含几个键—值对，也可能包含数百万个键—值对。鉴于字典可能包含
# 大量的数据，Python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种遍历字典的
# 方式：可遍历字典的所有键—值对、键或值。

# 1、遍历所有的键—值对
# 要编写用于遍历字典的for循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，可使用任何名称
# for语句的第二部分包含字典名和方法items()，它返回一个键—值对列表。
# 接下来，for循环依次将每个键—值对存储到指定的两个变量中。
print("========================== 遍历所有的键—值对")
user_0 = { 
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi', 
}
for key, value in user_0.items(): 
    print("Key: " + key) 
    print("Value: " + value)

# 2、遍历字典中的所有键
# 在不需要使用字典中的值时，方法keys()很有用。
print("========================== 遍历字典中的所有键")
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
}
for name in favorite_languages.keys(): 
    print(name.title())
# 遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_ 
# languages.keys():替换为for name in favorite_languages:，输出将不变
print("========================== 遍历字典中的所有键(省略key())")
for name in favorite_languages : 
    print(name.title())

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
} 
friends = ['phil', 'sarah'] 
for name in favorite_languages.keys(): 
    if name in friends: 
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")


# 3、按顺序遍历字典中的所有键
print("========================== 按顺序遍历字典中的所有键")
# 可使用函数sorted()来获得按特定顺序排列的键列表的副本
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
} 
for name in sorted(favorite_languages.keys()): 
    print(name.title())


# 4、遍历字典中的所有值
print("========================== 按顺序遍历字典中的所有值")
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
} 
for language in favorite_languages.values(): 
    print(language.title())

# 5、set剔除值重复项
# 为剔除重复项，可使用集合（set）。
# 集合类似于列表，但每个元素都必须是独一无二的
print("========================== set剔除值重复项")
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
} 
for language in set(favorite_languages.values()): 
    print(language.title())