str1="xiaoxie"
print(str1)
#### capitalize 字符串首字母大写 ####
print("\n----使字符串首字母大写----")
print("str1.capitalize(): ",str1.capitalize())    
str2 = "DAXIE"
print("\n----使字符串全部变小写----")
print(str2)
print("str2.casefold(): ",str2.casefold())
print("str2.lower(): ",str2.lower())
print("\n----使字符串全部变大写----")
print("str2.upper(): ",str2.upper())

print("\n----使字符串以width宽度居中----")
print("str2.center(20): ",str2.center(20))

print("\n----使字符串以width宽度左对齐----")
print("str2.ljust(20): ",str2.ljust(20))

print("\n----使字符串以width宽度右对齐----")
print("str2.rjust(20): ",str2.rjust(20))

str3 = "abcdefaaaa"
print("\n----判断字符串中某个字符出现次数----")
print(str3)
print("str3.count(\"a\"): ",str3.count("a"))
print("\n----判断字符串是否以某个字符结尾----")
print(str3)
print("str3.endswitch(\"a\"): ",str3.endswith("a"))

str4 = "I\tLOVE\tYOU"
print("\n----将\\t转换为空格----")
print(str4)
print("str4.expandtabs(): ",str4.expandtabs())

str5 = "i love you"
print("\n----检查某个字符是否在字符串中----")
print("str5.find(\"l\"): ",str5.find("l"))

str6 = "AbCdEfG"
print("\n----翻转字符串中大小写----")
print(str6)
print("str6.swapcase(): ",str6.swapcase())

str7 = "hello world, i love you"
print("\n----标题化----")
print(str7)
print("str7.title(): ",str7.title())