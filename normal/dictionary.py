

dict1 = {"李宁" : "一切皆有可能", "耐克" : "Just do it", "阿迪达斯" : "IImpossible is nothing"}
print("李宁的口号是： ", dict1["李宁"])

dict2 = {}
dict2.fromkeys((1,2,3))
print("dict2.fromkeys((1,2,3)): ", dict2.fromkeys((1,2,3)))
dict3 = {}
print("dict3.fromkeys((1,2,3),\"number\"): ", dict3.fromkeys((1,2,3),"number"))

dict4 = {}
dict4 = dict4.fromkeys(range(3), "赞")

for eachkey in dict4.keys() :
    print(eachkey)

for eachvalue in dict4.values() :
    print(eachvalue)

for eachitem in dict4.items() :
    print(eachitem)

print(dict4.get(100), "木有")
